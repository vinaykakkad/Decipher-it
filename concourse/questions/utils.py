import re

from datetime import datetime, timedelta, date
from django.contrib import messages

START_TIME =  datetime(2021, 1, 11, 11, 15, 0)
END_TIME =  datetime(2021, 2, 15, 23, 50, 0)


def only_letters(answer):
	'''
		Checks if the answer only contains lowercase english alphabets
	'''
	match = re.match("^[a-z0-9]*$", answer)
	return bool(match)


def is_hunt_active(user, round, request):
	'''
		Returns false if:
			- Hunt has not started or has ended
			- If the user is already disqualified
			- If the user is not able to submit the answer on time
	'''
	today = date.today()
	duration = round.duration
	delta = timedelta(minutes=duration)
	current_time = datetime.now()
	last_round_time = user.last_round_time

	# If the user is already disqualified
	if user.is_disqualified:
		messages.error(request, 
			'You are disqualified, you cannot proceed further')
		user.deactivate_countdown()
		return False

	# If the duration of the round is over and user has not completed it
	if (datetime.combine(today, last_round_time)) + delta < current_time and \
		user.current_que <= round.max_questions():
		user.deactivate_countdown()
		user.is_disqualified = True
		user.save()

		messages.error(request,
			'The countdown has finished, you cannot proceed further')
		return False

	# If the hunt is not active
	if not START_TIME <= current_time <= END_TIME:
		user.deactivate_countdown()
		messages.error(request, 
			'Concourse is not active yet')
		return False

	return True
