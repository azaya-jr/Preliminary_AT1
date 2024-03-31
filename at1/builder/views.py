import os
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm, AuthorForm, QuestionForm, AnswerForm

BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USER_DECKS_DIR = str(os.path.join(BASE_DIR, 'Local', 'My_Decks'))

# Ensure USER_DECKS_DIR exists
if not os.path.exists(USER_DECKS_DIR):
    os.makedirs(USER_DECKS_DIR)

def create_deck_folder(name):
    deck_path = str(os.path.join(USER_DECKS_DIR, name))
    os.makedirs(deck_path)
    os.makedirs(os.path.join(deck_path, 'Q'))
    os.makedirs(os.path.join(deck_path, 'A'))

def save_question_and_answer(name, question, answer):
    current_directory = str(os.path.dirname(os.path.abspath(__file__)))
    currentlog_path = str(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt'))
    if currentlog_path is None:
        return redirect("http://127.0.0.1:8000/login/")
    if current_directory is None:
        return redirect("http://127.0.0.1:8000/signup/")
    with open(currentlog_path, 'r') as currentlog_file:
        user_subdirectory = str(currentlog_file.read().strip())
    lpath = str(os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History')))
    dpath = str(os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/RecDeck/RecentDeck.txt')))
    if not os.path.exists(dpath):
        return redirect("http://127.0.0.1:8000/eduprod/")
    with open(dpath, 'r') as file:
        directory_name = str(file.read().strip())
    print("directory_name:", directory_name) 
    cpath = str(os.path.join(os.path.dirname(__file__), '..', 'Local', directory_name)) 
    print("dpath:", dpath)  # Add print statement to check dpath
    deck_path = str(os.path.join(USER_DECKS_DIR, name))
    q_folder = str(os.path.join(cpath, 'Q'))
    a_folder = str(os.path.join(cpath, 'A'))
    num_questions = len(os.listdir(q_folder))
    question_file = str(os.path.join(q_folder, f'{num_questions + 1}.txt'))
    answer_file = str(os.path.join(a_folder, f'{num_questions + 1}.txt'))
    with open(question_file, 'w') as q_file:
        q_file.write(str(question))
    with open(answer_file, 'w') as a_file:
        a_file.write(str(answer))

def create_deck(request):
    current_directory = str(os.path.dirname(os.path.abspath(__file__)))
    currentlog_path = str(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Local', 'currentlog.txt'))
    if currentlog_path is None:
        return redirect("http://127.0.0.1:8000/login/")
    if current_directory is None:
        return redirect("http://127.0.0.1:8000/signup/")
    with open(currentlog_path, 'r') as currentlog_file:
        user_subdirectory = str(currentlog_file.read().strip())
    lpath = str(os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/History')))
    dpath = str(os.path.normpath(os.path.join(current_directory, f'../../Local/{user_subdirectory}/RecDeck/RecentDeck.txt')))
    if not os.path.exists(dpath):
        return redirect("http://127.0.0.1:8000/eduprod/")
    if request.method == 'POST':
        name_form = NameForm(request.POST)
        author_form = AuthorForm(request.POST)
        question_form = QuestionForm(request.POST)
        answer_form = AnswerForm(request.POST)
        if name_form.is_valid() and author_form.is_valid():
            name = str(name_form.cleaned_data['name'])
            author = str(author_form.cleaned_data['author'])
            create_deck_folder(name)
            save_author(name, author)
            
            # Set 'deck_name' in session
            request.session['deck_name'] = name
            
            return HttpResponseRedirect('/deck_created/')  # Redirect to a success page
        elif question_form.is_valid() and answer_form.is_valid():
            name = str(request.session.get('deck_name'))
            question = str(question_form.cleaned_data['question'])
            answer = str(answer_form.cleaned_data['answer'])
            save_question_and_answer(name, question, answer)
            return HttpResponseRedirect(request.path)  # Redirect to the same page to allow adding more questions

    else:
        name_form = NameForm()
        author_form = AuthorForm()
        question_form = QuestionForm()
        answer_form = AnswerForm()

    return render(request, 'create_deck.html', {'name_form': name_form, 'author_form': author_form, 'question_form': question_form, 'answer_form': answer_form})
