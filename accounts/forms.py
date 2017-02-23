from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Family
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in xrange(2017, 2036)]
    family_1 = forms.CharField(label='Full Name')
    family_2 = forms.CharField(label='Family Member 2 Full Name')
    family_3 = forms.CharField(label='Family Member 3 Full Name')
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['number_family','email', 'password1', 'password2']
        exclude = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class FamilyForm(forms.ModelForm):
    '''
    def __init__(self, number_family, *args, **kwargs):
        super(FamilyForm, self).__init__(*args, **kwargs)
        for i in range(0, number_family):
            self.fields["first_name"] = forms.CharField()
            self.fields["last_name"] = forms.CharField()
            '''
    class Meta:
        model = Family
        exclude = ['account_name']



