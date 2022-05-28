import email
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from multiprocessing import Event
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .models import Partner, Slider,About, Gallery, Project, Team, News, AboutTiles, Contact, Event, Testomonial, Upcomming_Event,NewUser,Comment
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    # user = NewUser.objects.all()
    slider = Slider.objects.all()
    projects = Project.objects.all()
    abouts = About.objects.all()
    about_tiles = AboutTiles.objects.all()
    testomonials = Testomonial.objects.all()
    partners = Partner.objects.all()
    upcomming_events = Upcomming_Event.objects.order_by('-event_date')[:2]
    
    context = {
        # 'user':user,
        'slider':slider,
        'projects': projects,
        'abouts': abouts,
        'about_tiles': about_tiles,
        'upcomming_events': upcomming_events,
        'testomonials': testomonials,
        'partners':partners
    }
    return render(request, 'base/home.html', context)


def userProfile(request,pk):
    user=NewUser.objects.get(id=pk)
    context = {'user':user}
    return render(request, 'base/profile.html', context)


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        # print(request.user)
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # try:
        #     user = NewUser.objects.get(username=user_name)
        # except:
        #     messages.error(request, 'User doesnot exist')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # print("\n\n\n\n\n", request.user,"\n\n\n\n\n\n")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password doesnot exit")
        # import pdb; pdb.set_trace()
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured duing registration!!')
    return render(request, 'base/login_register.html', {'form': form})


def about(request):
    abouts = About.objects.all()
    about_tiles = AboutTiles.objects.all()
    context = {'abouts': abouts, 'about_tiles': about_tiles}
    return render(request, 'base/about.html', context)   


def aboutDetail(request, pk):
    about = AboutTiles.objects.get(id=pk)
    context = {'about': about}
    return render(request, 'base/aboutDetail.html', context)


def project(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/project.html', context)

def projectDetail(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'base/projectDetail.html', context)

def team(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'base/teams.html', context)

def event(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'base/events.html', context)

def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'base/eventsDetail.html', context)


def gallery(request):
    gallerys = Gallery.objects.all()
    context = {'gallerys':gallerys}
    return render(request, 'base/gallery.html',context)


def news(request):
    newses = News.objects.all()
    context = {'news': newses, }
    return render(request, 'base/news.html', context)


def newsDetail(request, pk):
    news = News.objects.get(id=pk)
    comments = news.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            news=news,
            body=request.POST.get('body')
        )
        return redirect('news', pk=news.id)

    context = {'news': news, 'comments': comments}
    return render(request, 'base/newsDetail.html', context)


@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse("You're not alllowed here!!")

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': comment})


def contact(request):
    if request.method == 'POST':
        # print(request.POST.get('name'))
        contact = Contact.objects.create(
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            phone_number=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        contact.save()
        return redirect('contact')

        # print(request.POST)
        # contacts = Contact(request.POST)
        # # contacts = Contact.create(
        # #     name=name,
        # #     subject=subject,
        # #     phone=phone,
        # #     message=message,

        # # )
        # if contacts.is_valid():
        #     contacts.save()
        #     return redirect('contact')
        # else:
        #     messages.error(request, 'An error occured duing registration!!')

    # contacts = Contact.objects.all()
    context = {}
    return render(request, 'base/contact.html', context)


