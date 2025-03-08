print("  *---井字棋---*")
number=['1','2','3','4','5','6','7','8','9']
def draw(lst):
    for i in range(3):
        print("    ",number[i],'|',number[i+1],'|',number[i+2])
        print("   +---+---+---+")
print(draw(number))