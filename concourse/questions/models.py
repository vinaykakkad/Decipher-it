from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


def lowercase_answer(value):
    if (value.islower()):
        return value
    else:
        raise ValidationError(
            _('%(value)s should not contain any capital letters'), 
            params = {'value': value}, 
        )


class Round(models.Model):
    number = models.IntegerField()
    key = models.CharField(max_length=50)
    duration = models.IntegerField()
    required_points = models.IntegerField()
    
    def __str__(self):
        return f'round_{self.number}'

    def max_questions(self):
        return len(self.questions.all())


class Question(models.Model):
    Question_Number = models.IntegerField()
    Question_Text = RichTextUploadingField()
    Question_Answer = models.CharField(max_length = 50)
    Question_Round = models.ForeignKey(Round, on_delete=models.CASCADE, 
                                        related_name='questions')

    def __str__(self):
        return f'{self.Question_Round}.{str(self.Question_Number)}'