# Media Control

Control Youtube, streaming sites, media players on your computer using your phone as a remote.

### Installation
`pip install -r requirements.txt`


### Usage

Run `python media-control.py` and open `http://[host_address]:[port]` provided in the terminal on your phone.


## Features

#### Youtube mode
![youtube remote screenshot](./screenshots/youtube-remote.png)

- Play/Pause
- Seek forward/backward in the video
- Enable/Disable captions
- Toggle fullscreen mode
- Go to next/previous video in a playlist
- Control Device volume

#### Universal mode
![universal remote screenshot](./screenshots/universal-remote.png)

- Play/Pause and playing media
- Go to next/previous media in queue
- Control Device volume


### Working

`Flask` app `media-control.py` serves a remote UI in `/` with `/control` as the API endpoint for POST requests made by `index.js`
[index.js](./remote/static/js/index.js) sends POST requests to the API using fetch with the button id and mode.
[controller.py](./controller.py) presses the right key/key-combination to control the host device using `pynput` package. 

## Server Details

Made using: Flask

flask is running on all addresses
in your current network.

Default host address = 0.0.0.0
Default port = 5000


- Check firewall if port 5000 is allowed or not.
- Change host to the local IP address of the device
you want to control.
- There is currently no security over this connection,
avoid using in a public network.


### Todo:

- Authentication
- SSL for security