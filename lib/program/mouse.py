from lib.cmd import Cmd
from autopilot.input import Mouse


class MouseCmd(Cmd):
    program_name = 'Mouse'

    def __init__(self):
        super(MouseCmd, self).__init__()
        self.mouse = Mouse.create()
        self.r = 10

    def direction(self, index):
        code_map = {
            13: [0, -1],
            15: [-1, 0],
            17: [1, 0],
            19: [0, 1],
        }
        if index in code_map:
            return code_map[index]
        return False

    def run(self, index):
        direction = self.direction(index)
        if direction:
            self.new_poss(direction[0], direction[1])
        elif index == 12:
            self.mouse.click(button=1)
        elif index == 16:
            self.mouse.click(button=2)
        elif index == 14:
            self.mouse.click(button=3)
        elif index == 18:
            self.r -= 10
            print(self.r)
        elif index == 20:
            self.r += 10
            print(self.r)

        if self.r < 10:
            self.r = 10

    def new_poss(self, x, y):
        (pos_x, pos_y) = self.mouse.position()
        self.mouse.move(pos_x + self.r * x, pos_y + self.r * y)