from lib.cmd import Cmd


class Chrome(Cmd):
    program_name = 'Chrome'

    def __init__(self):
        super(Chrome, self).__init__()

    def get_all_commands(self):
        return {
            3: {
                'command': ''
            },
            4: {
                'command': ''
            },
            5: {
                'command': ''
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
                'command': 'google-chrome --new-tab'
            },
            13: {
                'command': 'google-chrome --start-maximized'
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
