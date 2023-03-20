mine = """op: 0, reg1: 8, reg2: 0, imm: 8
op: 21, reg1: 6, reg2: 0, imm: 0
op: 16, reg1: 0, reg2: 0, imm: 12
op: 20, reg1: 1, reg2: 0, imm: 0
op: 2, reg1: 8, reg2: 0, imm: 8
op: 17, reg1: 0, reg2: 0, imm: 0
op: 18, reg1: 2, reg2: 0, imm: 0
op: 5, reg1: 6, reg2: 2, imm: 0
op: 8, reg1: 9, reg2: 0, imm: 2
op: 9, reg1: 9, reg2: 6, imm: 0
op: 10, reg1: 0, reg2: 0, imm: 16
op: 0, reg1: 6, reg2: 0, imm: 1
op: 16, reg1: 0, reg2: 0, imm: -28
op: 3, reg1: 2, reg2: 1, imm: 0
op: 15, reg1: 0, reg2: 0, imm: 4
op: 8, reg1: 1, reg2: 0, imm: 2
op: 19, reg1: 2, reg2: 0, imm: 0
op: 17, reg1: 0, reg2: 0, imm: 0"""

theirs = """op: 0, reg1: 8, reg2: 0, imm: 8
op: 21, reg1: 6, reg2: 0, imm: 0
op: 16, reg1: 0, reg2: 0, imm: 12
op: 20, reg1: 1, reg2: 0, imm: 0
op: 2, reg1: 8, reg2: 0, imm: 8
op: 17, reg1: 0, reg2: 0, imm: 0
op: 18, reg1: 2, reg2: 0, imm: 0
op: 5, reg1: 6, reg2: 2, imm: 0
op: 8, reg1: 9, reg2: 0, imm: 2
op: 9, reg1: 9, reg2: 6, imm: 0
op: 10, reg1: 0, reg2: 0, imm: 16
op: 0, reg1: 6, reg2: 0, imm: 1
op: 16, reg1: 0, reg2: 0, imm: -28
op: 3, reg1: 2, reg2: 1, imm: 0
op: 15, reg1: 0, reg2: 0, imm: 4
op: 8, reg1: 1, reg2: 0, imm: 2
op: 19, reg1: 2, reg2: 0, imm: 0
op: 17, reg1: 0, reg2: 0, imm: 0"""

print(mine == theirs)