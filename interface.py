import sys
import time
import pychromecast
from pychromecast.discovery import *

''' Acts as a simplified interface to the pychromecast library '''
class ChromeCast():
	def __init__(self, cast, media_controller, media_status):
		self.cast = cast
		self.mc = media_controller
		self.mso = media_status
	
	def get_info(self):
		return self.cast.__repr__()
	
	def pause_vid(self):
		self.mc.block_until_active()
		self.mc.pause()
	
	def play_vid(self):
		self.mc.block_until_active()
		self.mc.play()
	
	def stop_vid(self):
		self.mc.block_until_active()
		self.mc.stop()
	
	def get_vid_title(self):
		self.mc.block_until_active()
		return self.mso.title
	
	def set_volume_up(self, new_volume):
		return self.cast.volume_up(float(new_volume))
	
	def set_volume_down(self, new_volume):
		return self.cast.volume_down(float(new_volume))
	
	def get_current_time(self):
		self.mc.block_until_active()
		return self.mso.current_time
	
	def get_vid_length(self):
		self.mc.block_until_active()
		return self.mso.duration
	
	def set_current_time(self, new_time):
		self.mc.block_until_active()
		self.mc.seek(new_time)
	
	def rewind_vid(self):
		self.mc.block_until_active()
		self.mc.rewind()
	
	def disconnect(self):
		self.cast.disconnect()
	
	def reboot(self):
		self.mc.block_until_active()
		self.cast.reboot()
	
	def next_vid(self):
		self.mc.block_until_active()
		self.mc.queue_next()
		
	def prev_vid(self):
		self.mc.block_until_active()
		self.mc.queue_prev()


def main():

	CAST_NAME = "<YOUR_CHROMECAST_NAME>"
	cast = None
	
	# Keep trying to connect until wanted chromecast is online
	while (cast == None):
		chromecasts, browsers = pychromecast.get_chromecasts()
		try:
			# Loop through all the chromecasts in the house
			cast = next(cc for cc in chromecasts if cc.device.friendly_name == CAST_NAME)
		except:
			print("Chromecast not found")
			
	cast.wait()
	
	# Create the Media Controller
	mc = cast.media_controller
	
	# Media Status Object
	mso = mc.status
	
	# Create our interface
	control = ChromeCast(cast, mc, mso)
	
	# Provided Commands
	if sys.argv[1] == "help":
		print(["help, info, title, pause, play, stop, v++, v--, rewind, seek, curr_time, duration, time, prev, next, disconnect, reboot"])

	# Get General Info
	if sys.argv[1] == "info":
		print(control.get_info())
	
	# Get Video Title
	if sys.argv[1] == "title":
		print(control.get_vid_title())
	
	# Pause Video
	if sys.argv[1] == "pause":
		print(control.pause_vid())
	
	# Play Video
	if sys.argv[1] == "play":
		print(control.play_vid())
	
	# Stop Video
	if sys.argv[1] == "stop":
		print(control.stop_vid())
	
	# Turn Up Volume
	if sys.argv[1] == "v++":
		print(control.set_volume_up(sys.argv[2]))
	
	# Turn Down Volume
	if sys.argv[1] == "v--":
		print(control.set_volume_down(sys.argv[2]))
		
	# Rewind
	if sys.argv[1] == "rewind":
		print(control.rewind_vid())
	
	# Seek
	if sys.argv[1] == "seek":
		print(control.set_current_time(sys.argv[2]))
	
	# Get Current Time
	if sys.argv[1] == "curr_time":
		print(control.get_current_time())
	
	# Duration
	if sys.argv[1] == "duration":
		print(control.get_vid_length())
	
	# Get Time
	if sys.argv[1] == "time":
		print(str(int(control.get_current_time())) + "/" + str(int(control.get_vid_length())))
	
	# Previous Video
	if sys.argv[1] == "prev":
		print(control.prev_vid())
		
	# Next Video
	if sys.argv[1] == "next":
		print(control.next_vid())
	
	# Disconnect ChromeCast
	if sys.argv[1] == "disconnect":
		print(control.disconnect())
	
	# Reboot ChromeCast
	if sys.argv[1] == "reboot":
		print(control.reboot())
	

if __name__ == "__main__":
	main()