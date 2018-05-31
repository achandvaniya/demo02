import os
import datetime
from django.conf import settings
import time



def get_current_timestamp():
	timestamp = int(time.time())
	return timestamp

def check_or_create_dir(dir_name):
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)		

def check_and_create_folder_complete_path(file_type):
	base_root = "uploads"
	current_datetime = datetime.datetime.now() 
	check_or_create_dir(base_root)
	
	year = current_datetime.year
	base_root = base_root+"/"+str(year)
	check_or_create_dir(base_root)

	month = current_datetime.month
	base_root = base_root +"/"+str(month)
	check_or_create_dir(base_root)
	
	day = current_datetime.day
	base_root = base_root + "/"+str(day)
	check_or_create_dir(base_root)

	if file_type == 'video':
		base_root = base_root+"/video"
	else:
		base_root = base_root+"/image"

	check_or_create_dir(base_root)
	return base_root 


def get_path_dict_from_path(dirpath, paths, file_dir):
	path = dirpath.split("/uploads/")[-1]
	path_list = path.split("/")
	year, month, day, image = None, None, None, None
	if len(path_list) > 0:
		year = path_list[0]
		if year not in paths:
			paths[year] = {}
	
	if len(path_list) > 1:
		month = path_list[1]
		if month not in paths[year]:
			paths[year][month] = {}
	
	if len(path_list) > 2:
		day = path_list[2]
		if day not in paths[year][month]:
			paths[year][month][day] = {}
	
	if len(path_list) > 3:
		folder = path_list[3]
		if folder not in paths[year][month][day]:
			paths[year][month][day][folder] = []
		paths[year][month][day][folder].append(file_dir)
	return paths