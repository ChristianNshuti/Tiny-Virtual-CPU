from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 10",
    "LOAD R2 10",
    "ADD R1 R2",
    "ADD R1 R2",
    "LOAD R3 20",
    "ADD R3 R3",
    "ADD R1 R3",
    "PRINT R1",
    "HALT"
]

cpu.load_program(program)
cpu.run()

