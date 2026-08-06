class TinyCPU:
    def __init__(self):
        self.registers = {
            "R1": 0,
            "R2": 0,
            "R3": 0,
            "R4": 0,
        }

        self.memory = []
        self.pc = 0
        self.running = True


    def load_program(self,program):
        self.memory = program
        self.pc = 0
        self.running = True

    def run(self):
        while self.running:

            instruction = self.memory[self.pc]
            parts = instruction.split()
            self.pc += 1
