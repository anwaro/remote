from lib.cmd import Cmd


class Spotify(Cmd):
    program_name = 'Spotify'

    def __init__(self):
        super(Spotify, self).__init__()

    def get_all_commands(self):
        cmd = "dbus-send --print-reply" \
              " --dest=org.mpris.MediaPlayer2.spotify" \
              " /org/mpris/MediaPlayer2" \
              " org.mpris.MediaPlayer2.Player.{} "
        return {
            3: {
                'command': cmd.format('Previous')
            },
            4: {
                'command': cmd.format('Next')
            },
            5: {
                'command': cmd.format('PlayPause')
            },
            6: {
                'command': ''
            },
            7: {
                'command': ''
            },
            8: {
                'command': ''
            },
            12: {
                'command': ''
            },
            13: {
                'command': ''
            },
            14: {
                'command': ''
            },
            15: {
                'command': ''
            },
            16: {
                'command': ''
            },
            17: {
                'command': ''
            },
            18: {
                'command': ''
            },
            19: {
                'command': ''
            },
            20: {
                'command': ''
            },
        }
