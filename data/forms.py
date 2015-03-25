from django import forms
from .models import gel,miscImg,miscFile

class ImgUploadModelForm(forms.ModelForm):

    class Meta:
        model = miscImg
        fields = ['shortName', 'date','note','imgFile']