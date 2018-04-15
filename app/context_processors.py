from .forms import SignupForm

def signup_form(request):
    return {
         'signup_form' : SignupForm()
    }
