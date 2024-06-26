import os
import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

def get_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def get_random_file_contents(directory_path):
    files = os.listdir(directory_path)
    if not files:
        return None, None  # Return None for both file name and content if no files are found
    random_file = random.choice(files)
    random_file_path = os.path.join(directory_path, random_file)
    return random_file, get_file_contents(random_file_path)  # Return both file name and content

def flash_card_roulette(request):
    log_file_path = os.path.join(os.path.dirname(__file__), '..', 'Local', 'currentlog.txt')
    log = get_file_contents(log_file_path)
    if log is None:
        return redirect("http://127.0.0.1:8000/login/")
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
    if currentlog_path is None:
        return redirect("http://127.0.0.1:8000/login/")
    if current_directory is None:
        return redirect("http://127.0.0.1:8000/login/")
    with open(currentlog_path, 'r') as currentlog_file:
        user_subdirectory = currentlog_file.read().strip()
        #define paths
    lpath = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History/history.txt'))
    dpath = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/RecDeck/RecentDeck.txt'))
    cqpath = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/RecDeck/cq.txt'))
    if not os.path.exists(dpath):
        return redirect("http://127.0.0.1:8000/login/")
    print("dpath:", dpath)  # Add print statement to check dpath

    with open(dpath, 'r') as file:
        directory_name = file.read().strip()
    print("directory_name:", directory_name)  # Add print statement to check directory_name

    cpath = os.path.join(os.path.dirname(__file__), '..', 'Local', directory_name)
    print("cpath:", cpath)  # Add print statement to check cpath

    if not os.path.exists(cpath):
        return redirect("http://127.0.0.1:8000/eduprod/")

    folder_a_path = os.path.join(cpath, 'A')
    folder_q_path = os.path.join(cpath, 'Q')

    if not os.path.exists(folder_a_path) or not os.path.exists(folder_q_path):
        return redirect("http://127.0.0.1:8000/eduprod/")

    files_in_a = set(os.listdir(folder_a_path))
    files_in_q = set(os.listdir(folder_q_path))

    if not files_in_a.issubset(files_in_q):
        return redirect("http://127.0.0.1:8000/builder/create_deck/")

    random_q_file, random_q_file_content = get_random_file_contents(folder_q_path)
    print("random_q_file:", random_q_file)  # Add print statement to check random_q_file
    print("random_q_file_content:", random_q_file_content)  # Add print statement to check random_q_file_content
    
    if random_q_file_content is None:
        return redirect("http://127.0.0.1:8000/builder/create_deck/")
    with open(cqpath, 'w') as cq_file:
                cq_file.write(random_q_file_content)
    # Find corresponding file in folder A
    corresponding_file_path = os.path.join(folder_a_path, random_q_file)
    print("corresponding_file_path:", corresponding_file_path)  # Add print statement to check corresponding_file_path

    corresponding_file_content = get_file_contents(corresponding_file_path)
    print("corresponding_file_content:", corresponding_file_content)  # Add print statement to check corresponding_file_content

    context = {
        'random_q_file_content': random_q_file_content,
        'corresponding_file_content': corresponding_file_content
    }
    return render(request, 'flash_card_roulette.html', context)
