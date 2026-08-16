from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 10",
    "LOAD R2 0",
    "ADD R2 R1",
    "PRINT R2", 
    "JUMP 2"
]

cpu.load_program(program)
cpu.run()

