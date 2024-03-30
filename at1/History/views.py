from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
import os
from django.shortcuts import render

def history_view(request):
    # Define paths
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file_path = os.path.join(base_path, 'Local', 'currentlog.txt')
    
    # Read user directory from currentlog.txt
    with open(log_file_path, 'r') as log_file:
        user_directory = log_file.readline().strip()
    
    # Check if History directory exists
    current_directory = os.path.dirname(os.path.abspath(__file__))
    currentlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt')
    history_directory = os.path.normpath(os.path.join(current_directory, f'../../Local/{user_directory}/History/'))
    if not os.path.exists(history_directory):
        return HttpResponse("Error: You are not logged in.")
    history_file_path = os.path.join(history_directory, 'history.txt')
    with open(history_file_path, 'r') as history_file:
        history_data = history_file.read()

    # Read cline.txt
    cline_file_path = os.path.join(history_directory, 'cline.txt')
    with open(cline_file_path, 'r') as cline_file:
        cline_data = cline_file.read().splitlines()

    # Read wline.txt
    wline_file_path = os.path.join(history_directory, 'wline.txt')
    with open(wline_file_path, 'r') as wline_file:
        wline_data = wline_file.read().splitlines()

    # Count occurrences of strings in cline.txt
    cline_counts = {}
    for line in cline_data:
        cline_counts[line] = cline_counts.get(line, 0) + 1

    # Count occurrences of strings in wline.txt
    wline_counts = {}
    for line in wline_data:
        wline_counts[line] = wline_counts.get(line, 0) + 1

    return render(request, 'history.html', {
        'history_data': history_data,
        'cline_counts': cline_counts,
        'wline_counts': wline_counts,
    })
    pass