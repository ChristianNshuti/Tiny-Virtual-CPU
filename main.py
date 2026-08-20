from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 0",
    "LOAD R2 5",
    "LOAD R3 1",
    "CMP R1 R2",
    "JUMP_IF_LESS 5",
    "JUMP_IF_ZERO 9",
    "PRINT R1",
    "ADD R1 R3",
    "JUMP 3",        
    "HALT"     
]

cpu.load_program(program)
cpu.run()

