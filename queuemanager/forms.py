from django.forms import ModelForm

from .models import Job


class JobUploadForm(ModelForm):

    class Meta:
        model = Job
        fields = ('job_title', 'colour', 'file_path_stl')
