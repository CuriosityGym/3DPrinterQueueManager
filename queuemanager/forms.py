from django.forms import ModelForm

from .models import Job


class CandidateForm(ModelForm):

    class Meta:
        model = Job
        fields = ('job_title', 'colour', 'file_path_stl')
