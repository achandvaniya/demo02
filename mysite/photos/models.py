from __future__ import unicode_literals

from django.db import models
from mysite.utils import util, constants




def custom_upload_location(instance, filename):
	file_extension = filename.split(".")
	if file_extension[-1] in constants.VIDEO_FILES:
		file_type = "video"
	else:
		file_type = "image"
	path = util.check_and_create_folder_complete_path(file_type)
	timestamp = util.get_current_timestamp()
	path = path + "/" + str(timestamp)+"_"+filename
	return path

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=custom_upload_location)
    uploaded_at = models.DateTimeField(auto_now_add=True)
