from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
import requests
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login, authenticate
from django.contrib.auth import logout as dj_logout

# manager isn't available in 'auth.User' has been swapped for 'productai.User'
from django.contrib.auth import get_user_model
productai = get_user_model()

# Create your views here.


openai.api_key ="API_KEY"


def description(request):
    return render(request, 'form.html')

# except csrf token

@api_view(['GET', 'POST'])
def product(request):
    # request to openai and get response
    # methode GET
    if request.method == 'POST':
        # get the question from the url
        title = request.POST.get('title')
        print('title', title)
        description = request.POST.get('description')
        print('description', description)
        prompt = f"Product: {title}\nDescription: {description}\n"
        
        response = openai.Completion.create(
            engine="davinci",
            temperature=0.9,
            prompt=prompt,
            max_tokens=150,
        )
        # DALL-E to generate image
        gen_image = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        url = gen_image['data'][0]['url']
        print('url', url)
        x = response['choices'][0]['text']
        return render(request, 'index.html', {'x': x, 'url': url})




def login_page(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('email', email)
        print('password', password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            dj_login(request, user)
            return HttpResponse('login')
        else:
            return HttpResponse('Invalid credentials')
    else:
        return render(request, 'login.html')
    
    

def signup_page(request):
    return render(request, 'signup.html')

# register new user using productai.model.User

def  signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # save user in database using email and password
        user = productai(email = email, username= email, password =password)
        user.save()
        return HttpResponse('signup')
    else:
        return render(request, 'signup.html')
        