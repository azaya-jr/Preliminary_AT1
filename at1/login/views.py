import os
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username matches a folder name
        user_folder = os.path.join('C:\\Users\\azaya\\Preliminary_AT1\\Local', username)
        if os.path.exists(user_folder):
            # Check if the password matches
            password_file = os.path.join(user_folder, 'Private', 'psd.txt')
            if os.path.exists(password_file):
                with open(password_file, 'r') as f:
                    stored_password = f.read().strip()
                if password == stored_password:
                    # Write '0' to login.txt
                    login_flag_file = os.path.join(user_folder, 'Private', 'login.txt')
                    with open(login_flag_file, 'w') as f:
                        f.write('0')

                    # Change currentlog.txt to the username
                    current_log_file = os.path.join('C:\\Users\\azaya\\Preliminary_AT1\\at1\\Local', 'currentlog.txt')
                    with open(current_log_file, 'w') as f:
                        f.write(username)
                    
                    return HttpResponse(f'Welcome, {username}!')
                else:
                    return HttpResponse('Error: Incorrect password!')
            else:
                return HttpResponse('Error: Password file not found!')
        else:
            return HttpResponse('Error: Username not found!')
    else:
        return render(request, 'login.html')
