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
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            # Read the content of currentlog.txt
            currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
            with open(currentlog_path, 'r') as currentlog_file:
                user_subdirectory = currentlog_file.read().strip()

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
            
            # Check if the folder and files exist
            deck_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/Q'))
            if not os.path.exists(deck_path):
                return JsonResponse({'error': 'Deck not found or broken.'}, status=404)
            file_names = [f for f in os.listdir(deck_path) if os.path.isfile(os.path.join(deck_path, f))]
            if not file_names:
                return JsonResponse({'error': 'Deck not found or broken.'}, status=404)
            
            # Check if each file in folder Q has a corresponding file in folder A
            for file_name in file_names:
                if not os.path.exists(os.path.join(current_directory, f'../../Local/{user_subdirectory}/A/{file_name}')):
                    return JsonResponse({'error': 'Deck not found or broken.'}, status=404)

            # Hide the form and the current header
            return JsonResponse({'recent_deck_content': recent_deck_content})
        else:
            return JsonResponse({'error': 'Name not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

def display_random_question(request):
    # Read the content of currentlog.txt
    currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
    with open(currentlog_path, 'r') as currentlog_file:
        user_subdirectory = currentlog_file.read().strip()

    # Get the directory of the views.py file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Get the path of folder Q
    deck_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/Q'))
    # Get a list of file names in folder Q
    file_names = [f for f in os.listdir(deck_path) if os.path.isfile(os.path.join(deck_path, f))]

    if file_names:
        # Choose a random file
        random_file = random.choice(file_names)
        # Read the content of the random file
        with open(os.path.join(deck_path, random_file), 'r') as file:
            question_content = file.read()
        # Render the template with the question content and the random file name
        return render(request, 'my_template.html', {'question_content': question_content})
    else:
        return JsonResponse({'error': 'Deck not found or broken.'}, status=404)