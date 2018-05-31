import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo
import os, sys
from django.conf import settings
from mysite.utils import util, constants

class ProgressBarUploadView(View):
    def get(self, request):
        media_paths = {}
        files = []
        path = settings.MEDIA_ROOT + "/uploads"
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                file_path =  os.path.join(dirpath, f) 
                file_dir = {f: constants.RELATIVE_PATH + file_path.split("/media")[-1]}
                media_paths = util.get_path_dict_from_path(dirpath, media_paths, file_dir)                
        print media_paths
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/upload/index.html', {'photos': photos_list, 'media_paths': media_paths})

    def post(self, request):
        # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        time.sleep(1)  
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))
