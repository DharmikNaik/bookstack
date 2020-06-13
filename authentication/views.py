from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(True)
        else:
            print(False)

    return render(request, 'signup.html')
