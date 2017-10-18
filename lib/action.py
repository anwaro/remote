from lib.programs.chrome import chrome
from lib.programs.clementine import clementine
from lib.programs.spotify import spotify
from lib.programs.mouse import MouseCmd
from lib.programs.vlc import vlc
from lib.programs.volume import volume
from lib.program import Program
from lib.codes import CODES
from lib.cmd import Cmd


class Action:
    programs = []
    active_program_index = 0
    last_code = ''
    last_action_time = 0

    def __init__(self):
        self.init_programs()
        self.volume = Program(volume)
        self.cmd = Cmd()

    def init_programs(self):
        programs = [
            clementine,
            spotify,
            vlc,
            chrome,
            # mouse
        ]
        for program in programs:
            self.programs.append(Program(program))

    @staticmethod
    def get_code_index(code):
        if code in CODES:
            return CODES[code]
        return -1

    @staticmethod
    def convert_code(code):
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
        self.cmd.activate(self.get_program())

    def run(self, code):
        str_code = self.convert_code(code)
        code_index = self.get_code_index(str_code)

        if code_index < 0:
            return
        elif code_index < 3:
            self.change_program(code_index)
        elif code_index < 9:
            self.program_action(self.get_program(), code_index)
        elif code_index < 12:
            self.program_action(self.volume, code_index)
        else:
            self.program_action(self.get_program(), code_index)

    def program_action(self, program, index):
        program.set_index(index)
        self.cmd.run(program)
