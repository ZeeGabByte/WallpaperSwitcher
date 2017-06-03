# -*- coding: utf-8 -*-
import urllib3
import pickle


def import_img(url):
	"""download the picture from the url"""
	
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	
	nb_wallpapers = pickle.load(open("/home/gabriel/Documents/PythonProjects/Wallpaper/nb_wallpapers.p", "rb"))  + 1
	
	f = open(r'/home/gabriel/Documents/PythonProjects/Wallpaper/Wallpapers/{}.jpg'.format(nb_wallpapers), 'wb')
	f.write(r.data)
	f.close()
	
	pickle.dump(nb_wallpapers, open("nb_wallpapers.p", "wb"))


url = 'http://chromecastbg.alexmeub.com/images/1080_AF1QipMaHuZNH82g0_4TNg4AFw4dx1SZvMci51PAlufg.jpg'
url = 'http://chromecastbg.alexmeub.com/images/1080_AF1QipOoqNHUfMsZ_Djz8VG7UL1-P9LL89KfWXhfC5az.jpg'
url = 'http://chromecastbg.alexmeub.com/images/1080_AF1QipNSGlIyQnKXjJjAjELwUb60Ji58mfCGUo0nwxPR.jpg'
url = 'http://chromecastbg.alexmeub.com/images/1080_AF1QipOsjg_4FX4rZTfCAWZg215AveaQ3wglx8b4fiWj.jpg'

print("number of wallpapers: {}".format(pickle.load(open("/home/gabriel/Documents/PythonProjects/Wallpaper/nb_wallpapers.p", "rb")) + 1))

import_img(url)

print("number of wallpapers: {}".format(pickle.load(open("/home/gabriel/Documents/PythonProjects/Wallpaper/nb_wallpapers.p", "rb")) + 1))

