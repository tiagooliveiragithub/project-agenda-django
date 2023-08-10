from django.shortcuts import render
from django.contrib import messages
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    messages.info(request, 'Um texto qualquer')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
