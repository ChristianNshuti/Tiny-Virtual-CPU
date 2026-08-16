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
        while self.running and self.pc < len(self.memory) :

            # Fetch
            instruction = self.memory[self.pc]

            # Decode
            parts = instruction.split()

            # Execution comes next
            opcode = parts[0]
            if opcode == "LOAD":
                register = parts[1]
                value = int(parts[2])
                self.registers[register] = value

            elif opcode == "ADD":
                register1 = parts[1]
                register2 = parts[2]
                self.registers[register1] += self.registers[register2]

            elif opcode == "SUB":
                register1 = parts[1] 
                register2 = parts[2]
                self.registers[register1] -= self.registers[register2]

            elif opcode == "JUMP":
                self.pc = int(parts[1])
                continue

            elif opcode == "PRINT":
                register = parts[1]
                value = self.registers[register]
                print(value)

            elif opcode == "HALT":
                self.running = False


            #Move to next instruction
            self.pc += 1
