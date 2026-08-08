from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 5",
    "LOAD R2 10",
    "ADD R1 R2",
    "PRINT R1",
    "SUB R1 R2",
    "PRINT R1",
    "HALT"
]

cpu.load_program(program)
cpu.run()

