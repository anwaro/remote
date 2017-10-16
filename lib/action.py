from lib.program.chrome import Chrome
from lib.program.clementine import Clementine
from lib.program.spotify import Spotify
from lib.program.mouse import MouseCmd
from lib.program.vlc import Vlc
from lib.program.volume import Volume
from lib.codes import CODES


class Action:
    programs = []
    active_program_index = 0
    last_code = ''
    last_action_time = 0

    def __init__(self):
        self.init_programs()
        self.volume = Volume()

    def init_programs(self):
        self.programs.append(Clementine())
        self.programs.append(Spotify())
        self.programs.append(Chrome())
        self.programs.append(Vlc())
        self.programs.append(MouseCmd())

    def get_code_index(self, code):
        if code in CODES:
            return CODES[code]
        return -1

    def convert_code(self, code):
        return code.decode("utf-8")

    def timestamp(self):
        pass

    def get_program(self):
        return self.programs[self.active_program_index]

    def change_program(self, code):
        program_count = len(self.programs)
        if code == 0:
            self.active_program_index += (program_count - 1)
        elif code == 2:
            self.active_program_index += 1

        self.active_program_index %= program_count
        self.get_program().activate()

    def run(self, code):
        str_code = self.convert_code(code)
        code_index = self.get_code_index(str_code)
        if code_index < 0:
            pass
        elif code_index < 3:
            self.change_program(code_index)
        elif code_index < 9:
            self.get_program().run(code_index)
        elif code_index < 12:
            self.volume.run(code_index)
        else:
            self.get_program().run(code_index)
