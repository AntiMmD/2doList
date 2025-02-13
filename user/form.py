from django import forms
from .models import User
from task.models import Task

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email','password')

    def save(self, commit=True):
        user = super().save(commit=False)  # Don't save to DB yet. calls save method inside the forms.ModelForm
        user.set_password(self.cleaned_data['password'])  # Hash the password
        user.save()  # Now save to DB
        return user



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateTask(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['date_created','status','user',]
        widgets = {
            'expiration_date': forms.DateInput(
                attrs={
                    'type': 'date',})
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['description'].required = False  # Make 'description' optional
        self.fields['expiration_date'].required = False  # Make 'expiration_date' optional
        self.fields['priority'].required = False  # Make 'status' optional