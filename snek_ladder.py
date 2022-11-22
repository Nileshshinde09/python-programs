from random import randint
def run_dice():
    dice = randint(1,6)
    return dice
arr = []
for i in range(1,101):
    arr.append(i)

Ladder_end =[99,92,76,42,38,14,30,67]
Ladder_start = [80,71,28,21,1,4,8,50]
snek_start =[97,95,88,62,48,36,32]
snek_end = [78,56,24,18,24,6,10]
def exit_():
    print("congratulations you have won the game")
    exit()
def app():
    i = 1
    print(f"You are in {i} position")
    while 1:
        input_ = int(input("Enter 1 if you want role dice : "))
        if input_:
            dnum = run_dice()
            print(f"dice number is {dnum}")
            i += dnum
            if 100 < i:
                i -= dnum
                print(f"You required only {100-i}")
                while i ==100:
                    input_ = int(input("Enter 1 if you want role dice : "))
                    if input_:
                        dnum = run_dice()
                exit_()

            print(f"You are in {i} position")
            for index,num in enumerate(Ladder_start):
                if num ==i:
                    i = Ladder_end[index]
                    print(f"you got ladder {num} to {i}")
                    break
            for index,num in enumerate(snek_start):
                if num ==i:
                    i = snek_end[index]
                    print(f"you bitten by snake now , you go {num} to {i}")
                    break
    exit_()
if __name__=="__main__":
    app()



