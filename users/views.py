from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """ Register the new user"""
    if request.method != 'POST':
        # create a blank form.
        form = UserCreationForm()
    else:
        #Process the completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid:
            new_user = form.save()

            # Log the existing user and redirect to the home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display the blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)