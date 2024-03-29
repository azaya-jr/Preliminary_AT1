import os
import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def my_view(request):
    # Read the content of currentlog.txt
    currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
    with open(currentlog_path, 'r') as currentlog_file:
        user_subdirectory = currentlog_file.read().strip()

    # Get the directory of the views.py file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Calculate the file path of login.txt proportionally
    login_file_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/Private/login.txt'))
    
    # Check if login.txt exists and contains any content
    if os.path.exists(login_file_path) and os.path.getsize(login_file_path) > 0:
        # Render the template with the form
        return render(request, 'my_template.html', {'show_form': True, 'show_header': False})
    else:
        # Return an error message
        return HttpResponse("Error: You are not logged in.")

def process_data(request):
    # Read the content of currentlog.txt
    currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
    with open(currentlog_path, 'r') as currentlog_file:
        user_subdirectory = currentlog_file.read().strip()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            # Get the directory of the views.py file
            current_directory = os.path.dirname(os.path.abspath(__file__))
            # Calculate the file path of RecentDeck.txt proportionally
            file_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/RecDeck/RecentDeck.txt'))
            # Write content to the RecentDeck.txt file
            with open(file_path, 'w') as file:
                file.write(f"{name}")
            # Read content from the RecentDeck.txt file
            with open(file_path, 'r') as file:
                recent_deck_content = file.read()
            # Return JSON response with recent deck content
            os.makedirs(recent_deck_content)
            if os.path.exists(recent_deck_content):
             print("Deck found")
            else:
             print("Deck created")
            os.makedirs(os.path.join(recent_deck_content, 'Q'))
            os.makedirs(os.path.join(recent_deck_content, 'A'))
            return JsonResponse({'recent_deck_content': recent_deck_content})
        else:
            return JsonResponse({'error': 'Name not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
