print("*---井 字 棋---*")
list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("  1 | 4 | 7")
print("+---+---+---+")
print("  2 | 5 | 8")
print("+---+---+---+")
print("  3 | 6 | 9")
print("+---+---+---+")
def draw(list):
    for i in range(3):
        print(" ",list[i],'|',list[i+3],'|',list[i+6])
        print("+---+---+---+")
print(draw(list))
def check_winner(list):
    win_status=[
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,4,8],
        [2,4,6]
    ]
    for i in range(win_status):
        if list[i[0]] != "" and list[i[0]]==list[i[1]]==list[i[2]]:
            return list[i[0]]
    return 0
def main():
    count=0
    while:
    
if __name__ == "__main__"