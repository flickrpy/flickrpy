"""
This file is for the future Flickr Upload API method,
which will allow programs that wish to upload to flickr
the ability, if used with the Authentication module.
"""

# This is a really UGLY script at the moment
# I am only uploading my work in progress to SVN
# for those curious people.

# This script MAY work, though I get a auth error.

__author__ = "Joshua Henderson <joshhendo@gmail.com>"
__version__ = "$Rev: 2 $"
__date__ = "$Date: 2007-03-23 06:28:46 +1100 (Fri, 23 Mar 2007) $"
__copyright__ = "Copyright 2008 Joshua Henderson"

# This script may work. You will need to have the ofllowing
# filled out here, as well as a standard flickr.py setup!

API_KEY = ''
API_SECRET = ''

token = ""

# ~~This script is currently UNUSABLE!~~
# EDIT: This script MAY work, though I get a auth error (I could have copied
# and pased the wrong auth code). Use at own risk.

# I will add a message when it sort of works.
#
# This script will get very messy while I am
# making it, so bear with me.
#
# Joshua Henderson <joshhendo@gmail.com>

import flickr,urllib,urllib2
import hashlib


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

def authentication(token, **params):
	# I said this would get ugly
	# This has been copied straight from the _doget function
	# in flickr.py, but is not the entire funciton
	#
	# What I will do later is seperate the auth part of _doget
	# into it's own function so whenever I update this particular
	# code, it will update everything that uses it at one time.
	
	paramaters = ['API_KEY', 'auth_token']

	for item in params.items():
            paramaters.append(item[0])

        paramaters.sort()

        api_string = [API_SECRET]
        for item in paramaters:
            for chocolate in params.items():
                if item == chocolate[0]:
                    api_string.append(item)
                    api_string.append(chocolate[1])
            if item == 'method':
                api_string.append('method')
                api_string.append(method)
            if item == 'API_KEY':
                api_string.append('api_key')
                api_string.append(API_KEY)
            if item == 'auth_token':
                api_string.append('auth_token')
                api_string.append(token)
                    
        api_string2 = ''.join(api_string)
	print api_string2
	api_signature = hashlib.md5(api_string2).hexdigest()
        
	#no URL needed, just auth token and signature
        #url = url + '&auth_token=%s&api_sig=%s' % (token, api_signature) 
	return api_signature

print checkextension (imageToUpload)

# This page can be a real help: http://docs.python.org/lib/node578.html

input = open(imageToUpload,'r')
s = input.readlines()
post = urllib.urlencode({'photo': s, 'title': 'testupload', 'api_sig': authentication(token, title='testupload'), 'auth_token': token})

print post

# Error: Instead of uploading the text /home/josh/me.jpg,
# I need to open the file first using the file commands - Fixed!

response = urllib2.urlopen ('http://api.flickr.com/services/upload/', post)

for each in response:
	print each
	# API Key still needs to be made
# Still in debugging mode.
# Work in progress