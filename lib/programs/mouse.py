from lib.program import Program
from autopilot.input import Mouse


class MouseProgram(Program):
    name = 'Mouse'
    icon = 'mouse.png'

    def __init__(self):
        super(MouseProgram, self).__init__( {})
        self.mouse = Mouse.create()
        self.speed = 10

    @staticmethod
    def direction(index):
        code_map = {
            12: [0, -1],
            13: [-1, 0],
            15: [1, 0],
            16: [0, 1],
        }
        if index in code_map:
            return code_map[index]
        return False

    def run(self, index):
        direction = self.direction(index)
        if direction:
            self.new_poss(direction[0], direction[1])
        elif index == 14:
            self.mouse.click(button=1)
        elif index == 18:
            self.mouse.click(button=3)
        elif index == 17:
            self.speed = (self.speed + 100) % 200

    def new_poss(self, x, y):
        (pos_x, pos_y) = self.mouse.position()
        self.mouse.move(pos_x + self.speed * x, pos_y + self.speed * y)

    def get_command(self):
        self.run(self.index)
        return ''
