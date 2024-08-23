from django import forms


from student.models import Addaitems,RaSitems,Usitems,Naturalsitems


class AddaForm(forms.ModelForm):
    class Meta:
        model = Addaitems
        fields = ['stock']

class RasForm(forms.ModelForm):
    class Meta:
        model = RaSitems
        fields = ['stock']

class UsForm(forms.ModelForm):
    class Meta:
        model = Usitems
        fields = ['stock']

class NaturalsForm(forms.ModelForm):
    class Meta:
        model = Naturalsitems
        fields = ['stock']