<<<<<<< HEAD
# views.py

import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def my_view(request):
    # Get the directory of the views.py file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Calculate the file path of login.txt proportionally
    login_file_path = os.path.normpath(os.path.join(current_directory, '../../Local/user/login.txt'))
    # Check if login.txt exists and contains any content
    if os.path.exists(login_file_path) and os.path.getsize(login_file_path) > 0:
        # Render the template with the form
        return render(request, 'my_template.html')
    else:
        # Return an error message
        return HttpResponse("Error: You are not logged in.")

def process_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            # Get the directory of the views.py file
            current_directory = os.path.dirname(os.path.abspath(__file__))
            # Calculate the file path of RecentDeck.txt proportionally
            file_path = os.path.normpath(os.path.join(current_directory, '../../Local/user/RecDeck/RecentDeck.txt'))
            # Write content to the RecentDeck.txt file
            with open(file_path, 'w') as file:
                file.write(f"{name}")
            # Read content from the RecentDeck.txt file
            with open(file_path, 'r') as file:
                recent_deck_content = file.read()
            # Return JSON response with recent deck content
            return JsonResponse({'recent_deck_content': recent_deck_content})
        else:
            return JsonResponse({'error': 'Name not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 2eee140718b1c819aa6ae0d5603d24e5832a70fd
