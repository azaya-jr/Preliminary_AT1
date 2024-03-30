import os
import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.http import HttpResponse, JsonResponse

#def generate_random_hex_string(length):
    #yes, it isnt hex, i know
#   hex_characters = '0123456789abcdefghijklmnopqrstuvwxyz'
#  return ''.join(random.choice(hex_characters) for _ in range(length))
def extract_last_part(path):
    # Remove trailing slashes if any
    path = path.rstrip(os.sep)
    # Split the path by slashes
    parts = path.split(os.sep)
    # Extract the last part
    last_part = parts[-1]
    return last_part

def continue_action(request):
    # Placeholder for the continue action
    message = "Continue action placeholder message."

def no_action(request):
    # Placeholder for the no action
    message = "No action placeholder message."

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
def delete_all_lines(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)
def process_data(request):
    if request.method == 'POST':
        # Read the content of currentlog.txt
        currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
        with open(currentlog_path, 'r') as currentlog_file:
            user_subdirectory = currentlog_file.read().strip()

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
                
            # Create .md file in the specified directory ../../Local/{user_subdirectory}/History
            history_directory = os.path.join(os.path.dirname(file_path), '..', 'History')
            os.makedirs(history_directory, exist_ok=True)
            current_name = extract_last_part(name)
            text_ext = ".txt"
            realname = 'history' + text_ext
            md_file_name = os.path.basename(realname)
            md_file_path = os.path.join(history_directory, md_file_name)
            if os.path.exists(name):
                with open(md_file_path, 'r') as file:
                    first_line = file.readline()
                with open(md_file_path, 'w') as file:
                    file.write(recent_deck_content)
            else:
                with open(md_file_path, 'w') as file:
                    file.write(recent_deck_content)
            cline_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History/cline.txt'))
            wline_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History/wline.txt'))
            delete_all_lines(cline_path)
            delete_all_lines(wline_path)
            # Create directories for Q and A
            if os.path.exists(recent_deck_content):            
                print("Deck found")
            else:
                print("Deck created")
                os.makedirs(os.path.join(recent_deck_content, 'Q'))
                os.makedirs(os.path.join(recent_deck_content, 'A'))
            
            return JsonResponse({'recent_deck_content': recent_deck_content, 'show_modal': False})
        else:
            return JsonResponse({'error': 'Name not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

    



def handle_action(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action:
            if action == 'yes':
                # Handle action corresponding to Yes
                # For example:
                return JsonResponse({'response': 'Yes action handled.'})
            elif action == 'no':
                # Handle action corresponding to No
                # For example:
                return JsonResponse({'response': 'No action handled.'})
            else:
                # Handle invalid action
                return JsonResponse({'error': 'Invalid action.'}, status=400)
        else:
            # Handle case where action is not provided
            return JsonResponse({'error': 'Action not provided.'}, status=400)
    else:
        # Handle other HTTP methods (e.g., GET)
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    
    
    
    
import os
from django.http import HttpResponse

def get_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def handle_answer(request, answer):
    if request.method == 'GET':
        log_file_path = os.path.join(os.path.dirname(__file__), '..', 'Local', 'currentlog.txt')
        log = get_file_contents(log_file_path)
        if log is None:
            return HttpResponse("Error: Unable to locate log file.")

        random_q_file = "a test"  # Placeholder, you need to retrieve this value from the session

        if random_q_file is None:
            return HttpResponse("Error: Random question file not found in session.")

        current_directory = os.path.dirname(os.path.abspath(__file__))
        currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')

        with open(currentlog_path, 'r') as currentlog_file:
            user_subdirectory = currentlog_file.read().strip()

        # Set the paths for cline.txt and wline.txt
        cline_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History/cline.txt'))
        wline_path = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History/wline.txt'))

        # Write to cline.txt if answer is correct
        if answer == 'correct':
            with open(cline_path, 'a') as cline_file:
                cline_file.write(random_q_file + '\n')
            return HttpResponse("Answer recorded as correct.")

        # Write to wline.txt if answer is incorrect
        elif answer == 'incorrect':
            with open(wline_path, 'a') as wline_file:
                wline_file.write(random_q_file + '\n')
            return HttpResponse("Answer recorded as incorrect.")