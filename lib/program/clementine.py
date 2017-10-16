from lib.cmd import Cmd


class Clementine(Cmd):
    program_name = 'Clementine'

    def __init__(self):
        super(Clementine, self).__init__()

    def get_all_commands(self):
        return {
            3: {
                'command': 'clementine --previous'
            },
            4: {
                'command': 'clementine --next'
            },
            5: {
                'command': 'clementine --play-pause'
            },
            6: {
                'command': 'clementine --volume-down',
                'notify': 'Clementine Volume Down',
            },
            7: {
                'command': 'clementine --volume-up',
                'notify': 'Clementine Volume Up',
            },
        }