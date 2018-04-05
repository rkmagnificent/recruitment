from django import forms
from app.models import Resumes


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ApplicationForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date',
                                      'class': 'col-xs-12 form-control m-1'}))
    gender = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    address1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    address2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    applied_position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-xs-12 form-control m-1'}))
    terms_and_conditions = forms.ChoiceField(
        widget=forms.CheckboxInput(attrs={
            'class': 'col-xs-12 form-control m-1'}))


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resumes
        fields = ('resume_path', )
