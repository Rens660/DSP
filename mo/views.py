from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == "POST" and request.FILES['file']:
        # get form data
        file = request.FILES['file']
        title = request.POST['title']
        case_nr = request.POST['case_nr']
        description = request.POST['description']
        crime_type = request.POST['crime_type']
        uploaded_file = Upload.objects.create(
            file=file,
            title=title,
            case_nr=case_nr,
            description=description,
            crime_type=crime_type
        )
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file.file.url,
            "uploaded_file": uploaded_file
        })
    return redirect(index)