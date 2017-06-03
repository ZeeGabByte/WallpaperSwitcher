# -*- coding: utf-8 -*-
from gi.repository import Gio
from random import randint
import pickle
import os
import uuid
from time import sleep


def change_wallpaper(pic_path):
	"""change the wallpaper to the given of a jpg picture"""
	
	rd_filename = str(uuid.uuid4().hex)
	path = '/home/gabriel/Documents/PythonProjects/Wallpaper/Wallpapers/'
	os.rename(path + '0.jpg', path + 'old.jpg')  # old wallpaper
	os.rename(pic_path, path + rd_filename + '.jpg')  # future wallpaper
	os.rename(path + 'old.jpg', pic_path)  # old wallpaper
	
	SCHEMA = 'org.gnome.desktop.background'
	KEY = 'picture-uri'
	gsettings = Gio.Settings.new(SCHEMA)
	gsettings.set_string(KEY, 'file://' + path + rd_filename + '.jpg')
	
	sleep(1)
	os.rename(path + rd_filename + '.jpg', path + '0.jpg')  # actual wallpaper


if __name__ == '__main__':
	# setup:
	# nb_wallpapers = 6
	# pickle.dump(nb_wallpapers, open("nb_wallpapers.p", "wb"))
	
	nb_wallpapers = pickle.load(open('/home/gabriel/Documents/PythonProjects/Wallpaper/nb_wallpapers.p', 'rb'))
	wallpaper_idx = randint(1, nb_wallpapers)
	pic_path = '/home/gabriel/Documents/PythonProjects/Wallpaper/Wallpapers/{}.jpg'.format(wallpaper_idx)

	change_wallpaper(pic_path)

