from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from spark.authentication.forms import SignUpForm
from spark.feeds.models import Feed


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'authentication/signup.html', ctx)
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = '{0} juntou-se a rede.'.format(
                user.username, user.username)
            feed = Feed(user=user, post=welcome_post)
            feed.save()
            return redirect('/')

    else:
        ctx = {'form': SignUpForm()}
        return render(request, 'authentication/signup.html', ctx)
