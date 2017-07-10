from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sys
import twitter
import time
import pygame
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

api = twitter.Api(consumer_key='BqeKHaVy4Y7bUltpLuIUagA4y',consumer_secret='OxqsnUpMp5jBlMYdTntEjgUv6dceUc82CX9YS2Nitwp7ODSPN0',access_token_key='1392842840-6fHLrv7aHxgQHzZwidFeZrbiH5W4UdzS7Wfro1t',access_token_secret='b584M0NW3Plrn9yjKdf1DVHlZ4V4GOvEEk4LefXxkWZJ6')

#theUsersName = ''
theVolume = ''
volNum = 1


pygame.mixer.init()
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('login.html')
	
@app.route('/', methods=['POST'])
def do_admin_login():
	shouldRun = False
	theUsersName = request.form['handle']
	print(theUsersName)
	if request.form['volume'] == 'Low':
		volNum = 0.3
	elif request.form['volume'] =='Medium':
		volNum = 0.6
	else:
		volNum = 1
	theVolume = volNum
	print(theVolume)
	shouldRun = True
	playTweets(theUsersName, shouldRun)	
	return home()
	
def playTweets(username,shouldRun):
	currentTweet = ''
	lastTweet = ''
	currentStatus = api.GetUserTimeline(screen_name=username,count=1)
	for status in currentStatus:
		currentTweet = status.text
		firstTweetToPlay = username + ' last tweeted: ' + currentTweet
		downloadAndPlayAudio(firstTweetToPlay)
		lastTweet = currentTweet
		
	while shouldRun:
		currentStatus = api.GetUserTimeline(screen_name=username,count=1)
		for status in currentStatus:
			currentTweet = status.text
			if currentTweet != lastTweet:
				downloadAndPlayAudio(currentTweet)
				lastTweet = currentTweet
			else:
				print('skipped')
				time.sleep(2)
				
def downloadAndPlayAudio(tweetText):
	print('Now playing: ' + tweetText)
	text_to_speech = TextToSpeechV1(
    	username='f1a41b87-d977-4970-bd9a-96693a077c98',
	    password='ADLADdfoxMsY',
	    x_watson_learning_opt_out=True)  # Optional flag

	with open(join(dirname(__file__), 'output.ogg'),
			  'wb') as audio_file:
		audio_file.write(
			text_to_speech.synthesize(tweetText, accept='audio/ogg;codecs=vorbis',
									  voice="en-US_MichaelVoice"))
									#voice="en-US_AllisonVoice"))
	pygame.mixer.music.load('output.ogg')
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
					#print "Playing", pygame.mixer.music.get_pos()
					time.sleep(0.020)
 
 
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)