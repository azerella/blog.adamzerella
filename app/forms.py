from django import forms

class SignupForm(forms.Form):
    username = forms.EmailField(
            label=False,
            widget=forms.EmailInput(attrs={'placeholder':'email'}),
            max_length=100)

    def clean_username(self):
        data = self.cleaned_data['username']
        # TODO error check clean_username!
        return data
