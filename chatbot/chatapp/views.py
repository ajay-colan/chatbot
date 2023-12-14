from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random


def chat(request):
    return render(request, "chat.html")

# Create your views here.
@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        chat_message = request.POST.get('chat_message')
        greetings = [
        "Hello! How can I assist you today?",
        "Greetings! Is there anything specific you would like to know?",
        "Hi there! What brings you here?",
        "Good day! How may I help you?",
        "Hey! Feel free to ask me anything.",
        "Hello! I'm here to answer your questions.",
        "Hi! What can I do for you?",
        "Greetings! Let me know how I can assist you.",
        "Hello there! How can I be of service?",
        "Hi! Welcome! How may I assist you today?",
        "Good to see you! What can I help you with?",
        "Greetings and salutations! What brings you here?",
        "Hey there! How can I make your day better?",
        "Hello! What can I provide information on?",
        "Hi! Is there something specific you would like to know?",
        "Greetings! I'm here to help. What do you need?",
        "Hello! Feel free to ask me anything.",
        "Hi there! How may I assist you today?",
        "Good day! What can I do for you?",
        "Hello! I'm at your service. How may I help you?"
    ]

        response_data = {'message': random.choice(greetings)}
        return JsonResponse(response_data)