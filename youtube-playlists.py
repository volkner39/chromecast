import httplib2
import os
import sys
import time
import random

from oauth2client import client
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pychromecast
from pychromecast.controllers.youtube import YouTubeController
from casttube import YouTubeSession
import httplib2

CAST_NAME = "<YOUR_CHROMECAST_NAME>"

SERIAL_LIST = ["<playlist_id1>", "<playlist_id2>"]

CLIENT_ID = "<YOUR_CLIENT_ID>"
CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
REFRESH_TOKEN = "<YOUR_REFRESH_TOKEN>"
TOKEN_URI = "https://oauth2.googleapis.com/token"

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
USER_AGENT = 'YourAgent/1.0'


def main():

	os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
	
	PLAYLIST = {}
	
	# Authenticate OAuth2 with Google
	creds = client.GoogleCredentials(access_token=None, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, refresh_token=REFRESH_TOKEN, token_expiry=None, token_uri=TOKEN_URI, user_agent=USER_AGENT)

	http = creds.authorize(httplib2.Http())
	creds.refresh(http)

	# Build the service
	youtube = build(API_SERVICE_NAME, API_VERSION, http=http)
	
	# Randomize Playlists
	# Comment this line if you don't want randomized playlists
	random.shuffle(SERIAL_LIST)

	# Loop through each playlist
	for serials in SERIAL_LIST:

		# Retrieve video's JSON values
		request = youtube.playlistItems().list(
			part = "snippet,contentDetails",
			maxResults = 10,
			playlistId = serials
		)

		response = request.execute()
		
		# Get a list of playlist items
		list_of_videos = response.get('items')
		video_ids = []

		# For each playlist item, get the corresponding video id
		for vids in list_of_videos:
			content_details = vids.get('contentDetails')
			snippet = vids.get('snippet')
			# Region blocking, age-restriction, deleted vid - maybe, later ....
			
			# Check if video is private
			if snippet.get('title') != "Private video":
				video_ids.append(content_details.get('videoId'))
		
		PLAYLIST[serials] = video_ids
		
	# Combine all video id's together into Queue
	# Plays the videos in playlist in order
	x = PLAYLIST.values()
	queue = [j for i in x for j in i][::-1]
	
	# If you want to randomize the videos, uncomment below
	# random.shuffle(queue)

	cast = None
	
	# Keep trying to connect until wanted chromecast is online
	while (cast == None):
		chromecasts = pychromecast.get_chromecasts()
		try:
			# Loop through all the chromecasts in the house
			cast = next(cc for cc in chromecasts if cc.device.friendly_name == CAST_NAME)
		except:
			print("Chromecast Not Found")

	cast.wait()
	
	# Create Youtube Controller + Register it
	yt = YouTubeController()
	cast.register_handler(yt)
	
	# Create a new Youtube Session
	yt.start_session_if_none()
	s1 = yt._session
	s1._start_session()
	
	# Initialize the Queue to play
	s1._initialize_queue(queue[0])
	
	print("Queue Play Order: ")
	print("1. " + queue[0])
	order = 2
	
	# Add wanted video id's to the Queue
	for id in queue[1:]:
		print(str(order) + ". " + id)
		yt.add_to_queue(id)
		order += 1


if __name__ == "__main__":
	main()