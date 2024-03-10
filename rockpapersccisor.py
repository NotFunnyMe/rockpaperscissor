p1name = input("Enter player one name: ")
p2name = input("Enter player two name: ")

def rock_paper_scissor(num1,num2,bit1,bit2):
    p1 = int(num1[bit1])%3
    p2 = int(num2[bit2])%3

    if  player_one[p1] == player_two[p2]:
        print("Draw")
    elif player_one[p1] == "rock" and player_two[p2] == "scissor":
        print(f"{p1name} wins")
    elif player_one[p1] == "rock" and player_two[p2] == "paper":
        print(f"{p2name} wins")
    elif player_one[p1] == "paper" and player_two[p2] == "scissor":
        print(f"{p2name} wins")
    elif player_one[p1] == "paper" and player_two[p2] == "rock":
        print(f"{p1name} wins")
    elif player_one[p1] == "scissor" and player_two[p2] == "rock":
        print(f"{p2name} wins")
    elif player_one[p1] == "scissor" and player_two[p2] == "paper":
        print(f"{p1name} wins")

player_one = {0:"rock", 1:"paper", 2:"scissor"}
player_two = {0:"paper", 1:"rock", 2:"scissor"}

while 1:
    num1 = input(f"{p1name}, Enter your choice: ")
    num2 = input(f"{p2name},Enter your choice: ")
    bit1 = int(input(f"{p1name}, Enter your secret bit position : "))
    bit2 = int(input(f"{p2name}, Enter your secret bit position: "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n: ")
    if ch=='n':
        break