cmd = "dbus-send --type=method_call" \
      " --dest=org.mpris.MediaPlayer2.vlc" \
      " /org/mpris/MediaPlayer2" \
      " org.mpris.MediaPlayer2.Player.{}"

vlc = {
    'name': 'Vlc',
    'icon': 'vlc.png',

    'key': {
        13: {'cmd': cmd.format('Previous'), 'notify': ''},
        14: {'cmd': cmd.format('PlayPause'), 'notify': ''},
        15: {'cmd': cmd.format('Next'), 'notify': ''},
    }
}
