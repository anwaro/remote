volume = {
    'name': 'Volume',
    'icon': '',

    'key': {
        9: {'cmd': 'amixer -q -D pulse sset Master toggle', 'notify': ''},
        10: {'cmd': 'pactl set-sink-volume @DEFAULT_SINK@ "-3%"', 'notify': ''},
        11: {'cmd': 'pactl set-sink-volume @DEFAULT_SINK@ "+3%"', 'notify': ''},
    }
}


