from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.forms import LoginForm, ApplicationForm, ResumeUploadForm


def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.user.is_authenticated:  # already logged in
        return redirect("/application")
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/application")
    return render(request, "login.html", context)


def application_view(request):
    form = ApplicationForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "application.html", context)


def resume_upload(request, pk=1):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = ResumeUploadForm()
    return render(request, "upload_resume.html", {
        'form': form
    })


def recruiters_view(request):
    pass
