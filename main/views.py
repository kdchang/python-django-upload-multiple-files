from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import os.path
# The root path in this python project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _handle_uploaded_file(file):
    """Deal with file upload   
    """
    # Write the file to media folder
    destination = open(os.path.join(BASE_DIR, 'media/{}'.format(file.name)), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

def get_index(request):
    return render(request, 'index.html', {})

def post_upload_images(request):
    # Fetch multiple files to list
    files = request.FILES.getlist('files')

    # Iterate the multiple files
    for afile in files:
        _handle_uploaded_file(afile)

    return HttpResponseRedirect('/')
