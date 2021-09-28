from pynput.keyboard import Key, Controller
keyboard = Controller()



youtube_commands = {
    'play_pause': 'k',
    'yt_forward': 'l',
    'yt_rewind': 'j',
    'yt_captions': 'c',
    'yt_fullscreen': 'f'
}

def control(key):
    print(key, youtube_commands.keys())
    if key in youtube_commands.keys():
        print(key)
        keyboard.type(youtube_commands[key])