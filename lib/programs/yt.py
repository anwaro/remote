cmd = "bash ~/Dokumenty/python/youtube-player/yt {}"

yt = {
    'name': 'Youtube player',
    'icon': 'yt.png',

    'key': {
        10: {'cmd': cmd.format('show_toggle'), 'notify': ''},
        12: {'cmd': cmd.format('vol_up'), 'notify': ''},
        13: {'cmd': cmd.format('prev'), 'notify': ''},
        14: {'cmd': cmd.format('play_pause'), 'notify': ''},
        15: {'cmd': cmd.format('next'), 'notify': ''},
        16: {'cmd': cmd.format('vol_down'), 'notify': ''},
        17: {'cmd': cmd.format('delete'), 'notify': ''},
        18: {'cmd': cmd.format('download'), 'notify': ''},
    }
}

