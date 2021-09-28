from pynput.keyboard import Key, Controller
keyboard = Controller()



youtube_commands = {
    'play_pause': 'k',
    'yt_forward': 'l',
    'yt_rewind': 'j',
    'yt_captions': 'c',
    'yt_fullscreen': 'f',
    'playlist_previous': 'p',
    'playlist_next': 'n'
}

def control(key):
    if key in youtube_commands.keys():
        with keyboard.pressed(Key.shift):
            keyboard.type(youtube_commands[key])