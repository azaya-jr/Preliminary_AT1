import os
from django.shortcuts import render, redirect
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if the username directory already exists
        user_folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'Local', username)
        if os.path.exists(user_folder_path):
            # If the folder already exists, return an error
            messages.error(request, 'Folder with this username already exists.')
            return redirect('signup')  # Adjust the URL name if necessary
        else:
            # Create the user directory
            os.makedirs(user_folder_path)
            # Create subdirectories and files
            os.makedirs(os.path.join(user_folder_path, 'History'))
            os.makedirs(os.path.join(user_folder_path, 'Private'))
            os.makedirs(os.path.join(user_folder_path, 'RecDeck'))
            # Create files inside the Private folder
            with open(os.path.join(user_folder_path, 'History', 'history.txt'), 'w') as file:
                file.write('')
            with open(os.path.join(user_folder_path, 'History', 'cline.txt'), 'w') as cline_file:
                cline_file.write('')
            with open(os.path.join(user_folder_path, 'History', 'wline.txt'), 'w') as wline_file:
                wline_file.write('')
            with open(os.path.join(user_folder_path, 'Private', 'ysr.txt'), 'w') as ysr_file:
                ysr_file.write(username)
            with open(os.path.join(user_folder_path, 'Private', 'psd.txt'), 'w') as psd_file:
                psd_file.write(password)
            with open(os.path.join(user_folder_path, 'Private', 'login.txt'), 'w') as psd_file:
                psd_file.write
            # Create RecentDeck.txt inside the RecDeck folder
            open(os.path.join(user_folder_path, 'RecDeck', 'RecentDeck.txt'), 'a').close()
            # Create login.txt in the same directory as RecDeck, Pri    vate, and History
            messages.success(request, 'Folder created successfully.')
            return redirect('signup')  # Adjust the URL name if necessary
    else:
        return render(request, 'signup.html')
