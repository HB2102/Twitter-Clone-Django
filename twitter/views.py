from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Tweet
from django.contrib import messages
from .forms import TweetForm, SignUpForm, ProfilePicForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


def home(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, 'Your tweet has been posted.')
                return redirect('home')

        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'tweets': tweets, 'form': form})

    else:
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'home.html', {})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, 'You must be logged in to access this page')
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk).order_by('-created_at')

        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']

            if action == "unfollow":
                current_user_profile.follows.remove(profile)

            elif action == "follow":
                current_user_profile.follows.add(profile)

            current_user_profile.save()

        return render(request, 'profile.html', {'profile': profile, 'tweets': tweets})

    else:
        messages.success(request, 'You must be logged in to access this page')
        return redirect('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You logged in successfully!")
            return redirect('home')

        else:
            messages.success(request, "There was a problem with tour authentication. Please try again.")
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully.")
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome yo our family :) ")
            return redirect('home')

    return render(request, "register.html", {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            login(request, current_user)
            messages.success(request, "Your profile has been updated")
            return redirect('home')

        return render(request, "update_user.html", {'user_form': user_form, 'profile_form': profile_form})

    else:
        messages.error(request, "You must be logged in to access this page")
        return redirect('home')


def tweet_like(request, pk):
    if request.user.is_authenticated:
        tweet = get_object_or_404(Tweet, id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user)
        else:
            tweet.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))




    else:
        messages.success(request, ("You must be logged in to access this page"))
        return redirect('home')


def tweet_show(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    if tweet:
        return render(request, "show_tweet.html", {'tweet': tweet})
    else:
        messages.success(request, "This tweet does not exist")
        return redirect('home')
