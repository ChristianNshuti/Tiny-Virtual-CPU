from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 5",
    "LOAD R2 10",
    "CMP R1 R2",
    "JUMP_IF_LESS 6",
    "PRINT R1",
    "HALT",
    "PRINT R2",
    "HALT"
]

cpu.load_program(program)
cpu.run()

