import twitter
import time
import pygame

#API Keys
api = twitter.Api(consumer_key='BqeKHaVy4Y7bUltpLuIUagA4y',consumer_secret='OxqsnUpMp5jBlMYdTntEjgUv6dceUc82CX9YS2Nitwp7ODSPN0',access_token_key='1392842840-6fHLrv7aHxgQHzZwidFeZrbiH5W4UdzS7Wfro1t',access_token_secret='b584M0NW3Plrn9yjKdf1DVHlZ4V4GOvEEk4LefXxkWZJ6')

pygame.mixer.init()

#Get variables from webapp
theUsersName = 'NotJohnOliver'
soundFile = 'C:\Users\Scotty\Desktop\TwitterOliver\hangouts_message.ogg'
pygame.mixer.music.load(soundFile)
volumeOf = 1
pygame.mixer.music.set_volume(volumeOf)

statuses = api.GetUserTimeline(screen_name= theUsersName,count=1)
print([s.text for s in statuses])

pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    #print "Playing", pygame.mixer.music.get_pos()
    time.sleep(0.020)


statusSave = statuses

while True:
	statuses = api.GetUserTimeline(screen_name=theUsersName,count=1)
	if (statusSave != statuses):
		print([s.text for s in statuses])
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			#print "Playing", pygame.mixer.music.get_pos()
			time.sleep(0.020)
		statusSave = statuses
	else:
		print("skipped")
	time.sleep(2)



