from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from .models import *
from .forms import *
from django.http import JsonResponse
from django.utils import timezone
from django.conf import settings
import os
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
def upload_files(request):
    if request.method == 'POST' and request.FILES:
        folder_path = request.POST.get('folder_path')
        if folder_path:
            media_root = settings.MEDIA_ROOT
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    new_filepath = os.path.join(media_root, filename)
                    os.rename(filepath, new_filepath)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def move_files(request):
    if request.method == 'POST':
        folder_path = request.POST.get('folder_path')
        if folder_path:
            media_root = settings.MEDIA_ROOT
            try:
                for filename in os.listdir(folder_path):
                    filepath = os.path.join(folder_path, filename)
                    if os.path.isfile(filepath):
                        # Construct the new file path in the media folder
                        new_filepath = os.path.join(media_root, filename)
                        # Move the file to the media folder
                        os.rename(filepath, new_filepath)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
        else:
            return JsonResponse({'success': False, 'error': 'Folder path is missing'})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})
    import_files_from_media_folder()



def import_files_from_media_folder():
    media_folder = settings.MEDIA_ROOT
    for filename in os.listdir(media_folder):
        if filename.endswith('.txt'):  # Assuming text files
            filepath = os.path.join(media_folder, filename)
            # Get file size in bytes
            size = os.path.getsize(filepath)
            # Check if the file already exists in the database
            if not File.objects.filter(name=filename).exists():
                # Create a new File object and save it
                file = File.objects.create(
                    name=filename,
                    date_import=timezone.now(),
                    taille=size,
                    etat='not_treated'  # Initial state
                )
                file.save()

# Call the function to import files from the media folder
import_files_from_media_folder()

def prediction_submit(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            # Perform prediction or processing here using longitude and latitude
            predicted_moisture = perform_prediction(longitude, latitude)  # Example function for prediction
            # Render the prediction result template with the predicted moisture level
            return render(request, 'prediction_submit.html', {'predicted_moisture': predicted_moisture})
    else:
        form = PredictionForm()
    return render(request, 'prediction.html', {'form': form})

# Example function for prediction (replace with your actual prediction logic)
def perform_prediction(longitude, latitude):
    # Your prediction logic goes here
    # This is just a placeholder, replace with your actual prediction algorithm
    return 'Placeholder moisture level'