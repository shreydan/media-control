from pynput.keyboard import Key, Controller
keyboard = Controller()

media_commands = {
    'play_pause': Key.media_play_pause,
    'volume_down': Key.media_volume_down,
    'volume_up': Key.media_volume_up,
    'playlist_previous': Key.media_previous,
    'playlist_next': Key.media_next
}


youtube_commands = {
    'shortcuts': {
        'play_pause': 'k',
        'yt_forward': 'l',
        'yt_rewind': 'j',
        'yt_captions': 'c',
        'yt_fullscreen': 'f'
    },
    'shift': {
        'playlist_previous': 'p',
        'playlist_next': 'n',
    },
    'media': {
        'volume_down': Key.media_volume_down,
        'volume_up': Key.media_volume_up,
    }
}

def control(mode, key):
    if mode == 'YOUTUBE':

        if key in youtube_commands['shortcuts'].keys():
            keyboard.type(youtube_commands['shortcuts'][key])

        elif key in youtube_commands['shift'].keys():
            with keyboard.pressed(Key.shift):
                keyboard.type(youtube_commands['shift'][key])

        elif key in youtube_commands['media'].keys():
            keyboard.press(youtube_commands['media'][key])
            keyboard.release(youtube_commands['media'][key])
        

    elif mode == 'NORMAL':
        if key in media_commands.keys():
            keyboard.press(media_commands[key])
            keyboard.release(media_commands[key])