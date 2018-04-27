from django import forms

from .models import Subscriber


class SignupForm(forms.Form):
    username = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={'placeholder':'Email here!'}
        ),
        max_length=80)

    def clean_username(self):
        data = self.cleaned_data['username']

        if Subscriber.objects.filter(username=data).exists():
            raise forms.ValidationError("Subscriber: %s exists!" % data)
        Subscriber.objects.create(username=data)

        return data


class CommentForm(forms.Form):
    comment = forms.CharField()

    def clean_comment(self):
        data = self.cleaned_data['comment']
        # TODO error check clean_username!
        return data
