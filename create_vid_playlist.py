from oauth2client import client
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pychromecast
from pychromecast.controllers.youtube import YouTubeController
from casttube import YouTubeSession
import httplib2


CAST_NAME = "Living Room TV"

VIDEO_LIST = ["xRke0gTZgJc", "VYyDi5UD5eI", "b54RWqiSwds", "PsHbMzNxZYM", "pFLu9n1StDM", "UhSvGPovRJs", "CfXXMZK9grE", "ELfSfBiiNco"]


def main():
	chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[CAST_NAME])
	if not chromecasts:
		print('No chromecast with name "{}" discovered'.format(args.cast))
		sys.exit(1)

	cast = chromecasts[0]
	# Start socket client's worker thread and wait for initial status update
	cast.wait()

	# Create Youtube Controller + Register it
	yt = YouTubeController()
	cast.register_handler(yt)
	
	# Create a new Youtube Session
	yt.start_session_if_none()
	s1 = yt._session
	s1._start_session()
	
	
	# Initialize the Queue to play
	s1._initialize_queue(VIDEO_LIST[0])
	
	print("Queue Play Order: ")
	print("1. " + VIDEO_LIST[0])
	order = 2
	
	# Add wanted video id's to the Queue
	for id in VIDEO_LIST[1:]:
		print(str(order) + ". " + id)
		yt.add_to_queue(id)
		order += 1


if __name__ == "__main__":
	main()
	