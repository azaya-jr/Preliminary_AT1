import os
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def logout_view(request):
    current_log_file = os.path.join('C:\\Users\\azaya\\Preliminary_AT1\\at1\\Local', 'currentlog.txt')
    with open(current_log_file, 'w'):
        pass
    return render(request, 'logout.html')