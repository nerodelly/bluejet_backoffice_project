from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from .models import *
from .csv_importer import import_new_csv_files
from .forms import *
from django.http import JsonResponse
from .forms import UploadFileForm
from django.utils import timezone

@login_required
def index(request):
    # Assuming you want to pass the current user to the template
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)
@login_required
def show_database_files(request):
    # Add your logic here to retrieve database files
    # For example, you might query the database for files
 
    return render(request, 'show_database_files.html')

@login_required
def edit_database(request):

    return render(request, 'edit_database.html',)
@login_required
def database_actions(request):
    return render(request, 'database_actions.html')

@login_required
def analytics_(request):
    return render(request, 'analytics.html')


@login_required
def predictions_(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Handle form submission and show predictions
            # You can process the form data and render the predictions accordingly
            pass
    else:
        form = PredictionForm()
    return render(request, 'predictions.html', {'form': form})
def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(
                request, 'Nom d\'utilisateur ou mot de passe incorrect!')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def file_list_view(request):
    # Query all File objects from the database
    file_objects = File.objects.all()

    # Pass the file_objects to the template context
    return render(request, 'show_database_files.html', {'file_objects': file_objects})


def my_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or perform other actions after successful form submission
    else:
        form = FileForm()
    return render(request, 'show_database_files.html', {'form': form})
