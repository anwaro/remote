
cmd = "dbus-send --print-reply" \
              " --dest=org.mpris.MediaPlayer2.spotify" \
              " /org/mpris/MediaPlayer2" \
              " org.mpris.MediaPlayer2.Player.{} "

spotify = {
    'name': 'Spotify',
    'icon': 'spotify.png',

    'key': {
        3: {'cmd': cmd.format('Previous'), 'notify': ''},
        4: {'cmd': cmd.format('Next'), 'notify': ''},
        5: {'cmd': cmd.format('PlayPause'), 'notify': ''},
        6: {'cmd': '', 'notify': ''},
        7: {'cmd': '', 'notify': ''},
        8: {'cmd': '', 'notify': ''},
        12: {'cmd': '', 'notify': ''},
        13: {'cmd': '', 'notify': ''},
        14: {'cmd': '', 'notify': ''},
        16: {'cmd': '', 'notify': ''},
        17: {'cmd': '', 'notify': ''},
        18: {'cmd': '', 'notify': ''},
        19: {'cmd': '', 'notify': ''},
        20: {'cmd': '', 'notify': ''},
    }
}
