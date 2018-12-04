from django.forms import ModelForm

from .models import Job


class CandidateForm(ModelForm):

    class Meta:
        model = Job
