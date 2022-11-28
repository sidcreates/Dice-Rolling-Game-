import random

print(">>>>>>>>>>>WELCOME TO DICE ROLLING GAME<<<<<<<<<<<")
name = input("Enter your Name:- ")
d = "yes"
print("Hello!!!",name)
score = 0
while d=="yes":
    com = random.randint(1,6)
    user=int(input("Enter Your Choice:- "))
    print("Your Choice is",user)
    if user>6:
        print("Enter Valid input!!!!")
        print("Exiting....!!1*&&&")
        break
    if user==com:
        print("YOU WIN :)")
        score+=1
        print("Your score: ",score)
    else:
        print("You Loose:(")
        print("Computer Chooses:",com)
        print("Better Luck Next Time!!")
        print("Your score: ",score)
    print("for Continue Press Enter...")
    ext=input("For Exit press E:-")
    if ext=='E':
        print("Enter Valid Input....!!!1")

        print("EXITING.........!!!?*% ")
        break
print("Your Score: ",score)
