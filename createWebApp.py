#!/usr/bin/python

# template
#[Desktop Entry]
#Version=1.0
#Name=Name
#Exec=google-chrome --user-data-dir=/home/user/.name --app=https://webapp.com --class=Name
#Icon=/home/user/.name/name.png
#Type=Application
#StartupWMClass=Name

import sys, getopt
from os.path import expanduser
import os
import shutil

def printError():
	print('> usage: createWebApp.py [-o <outputfile>] -n <appname> -u <url> -i <icon>')
	print('> when I don not get a outputfile I write it to ~/.local/share/applications/<name>.desktop')
	print('> or createWebApp.py -h to see this')

def createFolder(f):
	if not os.path.exists(f):
		os.makedirs(f)
	else:
		print('> Sorry, the folder ' + f + ' exists alredy.')
		print('> Please delete the folder or choose another name for your app.')
		sys.exit(2)

def getAppFolder(name):
	home = expanduser("~")
	return home + '/.' + name.lower()

def getIcon(icon, appfolder):
	dest = appfolder + '/' + appfolder.split('/')[-1][1:] + '.' + icon.split('/')[-1].split('.')[-1]
	shutil.copy(icon, dest)
	return dest
	
def getFileName(f, name):
	if f == '':
		return expanduser("~") + '/.local/share/applications/' + name + '.desktop'
	else:
		return f

def createApp(f, name, url, icon):
	

	f = open(f, "w", encoding='utf-8')
	f.write('[Desktop Entry]\n')
	f.write('Version=1.0\n')
	f.write('Name=' + name + '\n')
	f.write('Exec=google-chrome --user-data-dir=' + getAppFolder(name) + ' --app=' + url + ' --class=' + name + '\n')
	f.write('Icon=' + icon + '\n')
	f.write('Type=Application\n')
	f.close()

def main(argv):
	outputfile = ''
	name = ''
	url = ''
	icon = ''
	
	try:
		opts, args = getopt.getopt(argv,"ho:n:u:i:",["out=","name=","url=","icon="])
	except getopt.GetoptError:
		printError()
		sys.exit(2)
		
	for opt, arg in opts:
		if opt == '-h':
			printError()
			sys.exit()
		elif opt in ("-n", "--name"):
			name = arg
		elif opt in ("-o", "--out"):
			outputfile = arg
		elif opt in ("-u", "--url"):
			url = arg
		elif opt in ("-i", "--icon"):
			icon = arg
	
	if name == '' or url == '' or icon == '':
		printError()
		sys.exit(2)
		
	appfolder = getAppFolder(name)
	createFolder(appfolder)
	icon = getIcon(icon, appfolder)
	f = getFileName(outputfile, name)
	createApp(f, name, url, icon)

if __name__ == "__main__":
	main(sys.argv[1:])
