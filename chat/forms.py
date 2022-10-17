# from django import forms
# from chat.models import Messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(label='password', widget=forms.PasswordInput)  # PasswordInput hides the the password input

#     class Meta:
#         model = User
#         fields = ('username', 'password')

#     def clean(self): # here self is form
#         if self.is_valid():
#             # this clean method runs before anything in the forms
#             username = self.cleaned_data['username']
#             password = self.cleaned_data['password']

#             if not authenticate(username=username, password=password): # here if anything in this email and password entered is wrong..then it will raise the error
#                 raise forms.ValidationError("Invalid Data")





















# class MessagesForm(forms.ModelForm):
#     class Meta:
#         model = Messages
#         fields = ('message',)
#         # widgets = {
#         #     'message': forms.TextInput(attrs={'class':'form-control', 'placeholder':'message placeholder'})
#         # }
        