general = {
    'name': 'General',
    'icon': '',

    'key': {
        0: {'cmd': 'systemctl suspend', 'notify': ''},
        8: {'cmd': 'pactl set-sink-volume @DEFAULT_SINK@ "-3%"', 'notify': ''},
        9: {'cmd': 'pactl set-sink-volume @DEFAULT_SINK@ "+3%"', 'notify': ''},
        28: {'cmd': 'amixer -q -D pulse sset Master toggle', 'notify': ''},
    }
}
