from datetime import datetime, timedelta, date

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Question, Round
from .utils import only_letters, is_hunt_active

TOTAL_POINTS = 15


class RoundsView(LoginRequiredMixin, View):

    def get(self, request):
        rounds = Round.objects.all()
        current_round = Round.objects.get(number=request.user.current_round)
        max_questions = current_round.max_questions()

        context = {'rounds': rounds, 'max_questions': max_questions}
        return render(request, 'rounds.html', context)

    def post(self, request):
        '''
            Will detect if:
                - The post request was tampered

            If no error:
                - Set round, que
                - Activate countedown
        '''
        round_number, round = None, None
        user = request.user

        try:
            round_number = int(request.POST.get('round'))
        except Exception as identifier:
            pass

        if round_number is None:
            messages.error(request,
                           'There was some error in your request, please try again !!')
            return redirect('rounds')


        try:
            round = Round.objects.get(number=round_number)
        except Exception as identifier:
            pass

        if round is None:
            messages.error(request,
                           'There was some error in your request, please try again !!')
            return redirect('rounds')
        

        # Checking for the error
        if user.current_round+1 != round_number:
            messages.error(request,
                           'You can only activate the next round!!')
            return redirect('rounds')
        else:
            current_round = Round.objects.get(number=user.current_round)
            if user.current_ques != current_round.max_questions()+1:
                messages.error(request,
                            'You need to complete all the question to activate\
                            the round!!')
                return redirect('rounds')

            user.activate_countdown()
            user.current_que = 1
            user.set_round()
            user.save()

            return redirect('questions')


class QuestionView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        question_number = user.current_que
        round_number = user.current_round
        round = Round.objects.get(number=round_number)

        # Checking if the hunt is active for the user
        active = is_hunt_active(user, round, request)
        if not active:
            return redirect('rounds')

        # If the user has completed all the questions
        total_ques = round.max_questions()
        if question_number == total_ques+1:
            return redirect('congo')

        question = Question.objects.get(Question_Number=question_number,
                                        Question_Round=round)

        context = {'question': question}
        return render(request, 'questions.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        round_number = user.current_round
        round = Round.objects.get(number=round_number)

        # To check if the user has submitted on time
        is_hunt_active(user, round, request)

        question_number = user.current_que
        question = Question.objects.get(Question_Number=question_number,
                                        Question_Round=round)

        answer = request.POST.get('answer')

        # If the format of the answer is incorrect
        if not only_letters(answer):
            messages.error(
                request, 'Answer should only contain lower-case alphabets \
                    or numbers without spaces')
            return redirect('questions')

        # Updating user if answer is correct
        if answer == question.Question_Answer:
            user.set_current_que()
            user.set_last_ans_time()
            user.set_points()

            # Deactivating countdown if the round is completed
            total_ques = round.max_questions()
            if user.current_que == total_ques+1:
                user.deactivate_countdown()
                return redirect('congo')

            messages.info(request, 'Correct Answer!!')
            return redirect('questions')
        else:
            messages.error(request, 'WrongAnswer!!')
            return redirect('questions')


@login_required
def congo_view(request, *args, **kwargs):
    user = request.user
    has_completed_all = False

    round = user.current_round

    total_ques = (Round.objects.get(number=round)).max_questions()
    if user.current_que != total_ques + 1:
        messages.error(request,
            'You need to complete the round to access the page')
        return redirect('home')

    if user.points == TOTAL_POINTS:
        has_completed_all = True

    context = {'has_completed_all': has_completed_all}
    return render(request, 'congratulations.html', context)
