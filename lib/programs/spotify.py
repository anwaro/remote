
cmd = "dbus-send --print-reply" \
              " --dest=org.mpris.MediaPlayer2.spotify" \
              " /org/mpris/MediaPlayer2" \
              " org.mpris.MediaPlayer2.Player.{} "

spotify = {
    'name': 'Spotify',
    'icon': 'spotify.png',

    'key': {
        13: {'cmd': cmd.format('Previous'), 'notify': ''},
        14: {'cmd': cmd.format('PlayPause'), 'notify': ''},
        15: {'cmd': cmd.format('Next'), 'notify': ''},
    }
}
