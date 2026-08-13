from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 7",
    "LOAD R2 8",
    "ADD R1 R2",
    "LOAD R3 4",
    "LOAD R4 6",
    "ADD R3 R4",
    "SUB R1 R3",
    "PRINT R1",
    "HALT"
]

cpu.load_program(program)
cpu.run()

