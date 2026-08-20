from cpu import TinyCPU

cpu = TinyCPU()

program = [
    "LOAD R1 10",          
    "LOAD R2 5",          
    "CMP R1 R2",           
    "JUMP_IF_LESS 6",      
    "JUMP_IF_ZERO 8",      
    "JUMP_IF_GREATER 10",  
    "PRINT R1",            
    "HALT",                
    "PRINT R2",            
    "HALT",                
    "PRINT R1",            
    "HALT"                 
]

cpu.load_program(program)
cpu.run()

