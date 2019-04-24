from lib.programs.chrome import chrome
from lib.programs.clementine import clementine
from lib.programs.spotify import spotify
from lib.programs.yt import yt
from lib.programs.mouse import MouseProgram
from lib.programs.vlc import vlc
from lib.programs.general import general
from lib.program import Program
from lib.codes import CODES
from lib.cmd import Cmd
import copy


class Action:
    programs = []
    active_program_index = 0
    last_code = ''
    last_action_time = 0

    def __init__(self):
        self.init_programs()
        self.cmd = Cmd()

    def init_programs(self):
        programs = [
            clementine,
            yt,
            spotify,
            vlc,
            chrome,
        ]
        for program in programs:
            self.programs.append(Program(self.dict_merge(general, program)))
        self.programs.append(MouseProgram())

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
        if code == 6:
            self.active_program_index += 1

        self.active_program_index %= program_count
        self.cmd.activate(self.get_program())

    def run(self, code):
        str_code = self.convert_code(code)
        code_index = self.get_code_index(str_code)

        if code_index < 0:
            return
        elif code_index == 6 or code_index == 7:
            self.change_program(code_index)
        else:
            self.program_action(self.get_program(), code_index)

    def program_action(self, program, index):
        program.set_index(index)
        self.cmd.run(program)

    def dict_merge(self, dct, merge_dct):
        new_dct = copy.deepcopy(dct)
        for k, v in merge_dct.items():
            if k in dct and isinstance(dct[k], dict) and isinstance(merge_dct[k], dict):
                new_dct[k] = self.dict_merge(dct[k], merge_dct[k])
            else:
                new_dct[k] = copy.deepcopy(merge_dct[k])
        return new_dct
