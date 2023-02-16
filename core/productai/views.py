from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
import requests
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.


openai.api_key = "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"

@api_view(['GET'])
def index(request):
    # request to openai and get response
    # methode GET
    if request.method == 'GET':
        # get the question from the url
        title = request.GET.get('title')
        print('title : ', title)
        description = request.GET.get('description')
        print('description : ', description)
        prompt = f"Product: {title}\nDescription: {description}\n"
        
        response = openai.Completion.create(
            engine="davinci",
            temperature=0.9,
            prompt=prompt,
            max_tokens=150,
        )
        
        x = response['choices'][0]['text']
        return render(request, 'index.html', {'x': x})





