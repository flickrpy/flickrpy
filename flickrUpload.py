"""
This file is for the future Flickr Upload API method,
which will allow programs that wish to upload to flickr
the ability, if used with the Authentication module.
"""

# This script is currently UNUSABLE!
# I will add a message when it sort of works.
#
# This script will get very messy while I am
# making it, so bear with me.
#
# Joshua Henderson <joshhendo@gmail.com>
# This Software is GPLv3 protected(tm)

import flickr,urllib,urllib2

# This is a temp variable to test functions with
imageToUpload = "/home/josh/me.jpg"

def checkextension (image):
	check = 0
	extension = ""
	for each in image:
		if check:
			extension = extension + each
		if each == ".":
			check = 1
			# When I said this script will be messy
			# I meant it!
	return extension

print checkextension (imageToUpload)

# This page can be a real help: http://docs.python.org/lib/node578.html

post = urllib.urlencode({'photo': imageToUpload, 'title': 'test upload'})

# Error: Instead of uploading the text /home/josh/me.jpg,
# I need to open the file first using the file commands

responce = urllib2.urlopen ('http://api.flickr.com/services/upload/', post)

for each in responce:
	print each
	# API Key still needs to be made
# Still in debugging mode.
# Work in progress