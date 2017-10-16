from lib.cmd import Cmd


class Volume(Cmd):

    def __init__(self):
        super(Volume, self).__init__()

    def get_all_commands(self):
        return {
            9: {
                'command': 'amixer -q -D pulse sset Master toggle'
            },
            10: {
                'command': 'pactl set-sink-volume 0 "-3%"'
            },
            11: {
                'command': 'pactl set-sink-volume 0 "+3%"'
            },
        }

