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
        self.flags = {
            "LESS": False,
            "ZERO": False,
            "GREATER": False
        }


    def load_program(self,program):
        self.memory = program
        self.pc = 0
        self.running = True

    def run(self):
        while self.running and self.pc < len(self.memory) :
            # Fetch
            instruction = self.fetch()
            # Decode
            parts = self.decode(instruction)
            # Execution comes next
            self.execute(parts)


    def fetch(self):
        return self.memory[self.pc]

    def decode(self, instruction):
        return instruction.split()
    
    def execute(self,parts):
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
            return

        elif opcode == "JUMP_IF_LESS":
            if self.flags["LESS"]:
                self.pc = int(parts[1])
                return

        elif opcode == "JUMP_IF_ZERO":
            if self.flags["ZERO"]:
                self.pc = int(parts[1])
                return

        elif opcode == "JUMP_IF_GREATER":
            if self.flags["GREATER"]:
                self.pc = int(parts[1])
                return

        elif opcode == "PRINT":
            register = parts[1]
            value = self.registers[register]
            print(value)

        elif opcode == "CMP":
            reg1 = parts[1]
            reg2 = parts[2]
            register1 = self.registers[reg1]
            register2 = self.registers[reg2]

            self.flags["LESS"] = False
            self.flags["ZERO"] = False
            self.flags["GREATER"] = False

            if register1 < register2:
                self.flags["LESS"] = True

            elif register1 == register2:
                self.flags["ZERO"] = True

            elif register1 > register2:
                self.flags["GREATER"] = True

        elif opcode == "HALT":
            self.running = False

        #Move to next instruction
        self.pc += 1
     