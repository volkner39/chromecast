# Chromecast Controller


## Dependencies:
* Python 3.5+
* pip install --upgrade google-api-python-client
* pip install --upgrade google-auth-oauthlib google-auth-httplib2
* pip install pychromecast
* pip install casttube
* pip install httplib2
* pip install oauth2client

---

## interface.py

A simplified version of the pychromecast library. Now you can control your chromecast with easy to remember commands, from the leisure of your command line.

### Usage:

* Get List of Commands Supported: ``` python interface.py help ```

* Get Basic ChromeCast Info: ``` python interface.py info ```

* Get Currently Playing Video Title: ``` python interface.py title ```

* Pause Currently Playing Video: ``` python interface.py pause ```

* Resume Paused Video: ``` python interface.py play ```

* Stop Currently Playing Video: ``` python interface.py stop ```

* Turn Up Volume: ``` python interface.py v++ 0.1 ```

* Turn Down Volume: ``` python interface.py v-- 0.5 ```

* Rewind Video: ``` python interface.py rewind ```

* Skip to Specific Time: ``` python interface.py seek 1200```

* Get Current Time of Playing Video: ``` python interface.py curr_time ```

* Get Total Time of Playing Video: ``` python interface.py duration ```

* Get Current and Total Time of Playing Video: ``` python interface.py time ```

* Play Previous Video from Queue: ``` python interface.py prev ```

* Play Next Video in Queue: ``` python interface.py next ```

* Disconnect Current Program: ``` python interface.py disconnect ```

* Reboot Chromecast: ``` python interface.py reboot ```

---

## youtube-playlists.py

Connects to the Youtube API. Grabs a given number of videos of different playlists and plays them on the chromecast. Will play 10 videos from a given playlist by default. Created this mainly for my grandma, but could help anyone else too!

### Usage:

``` python youtube-playlists.py ```

First, you need to create your unique Youtube API key and OAuth ID. 
This can be done here: https://console.developers.google.com/?pli=1

Create a new project and enable the Youtube Data API v3 by searching for it in the API Library.

When creating the OAuth ID, make sure you choose Web Application. Provide the re-direct URI - https://developers.google.com/oauthplayground/.

Then, you need to get a refresh token here: https://developers.google.com/oauthplayground/.

In the OAuth 2.0 configuration settings menu on the top-right, select the box "Use your own OAuth credentials".
Enter your Client ID and Client Secret. If you get a URI error, you didn't provide the link above.

Next, choose Youtube Data API v3 and select the scope "youtube.readonly". Now, you can replace the fields in my script with your keys!
The <playlist_id> is the id of the youtube playlist you want to watch. You can find this in the youtube link of the playlist.

---

### Issues:
* The script skips private videos. For now, I did not include cases such as age-restriction, geo-blocking, deleted vids, etc.

* The script will constantly try to connect to the chromecast until it's available, so please be patient.

* If you want to randomize videos or increase the # of videos retrieved just read the comments to comment/uncomment.

* Only tested for Chromecast 2 on Windows and Linux


Will document this more later.
Let me know if you want any features or if there are any bugs.
