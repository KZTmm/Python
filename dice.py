import random
name=input("Enter your name: ")
password=input("Enter your password: ")

if not(name=='kyaw' and password=='1234'):
    print("Wrong name or password!")
else:
    print("Correct name or password!")


balance=0
balance=int(input("How much do you buy?: "))
print(f"Your current balance: {balance}")


while True:

    print("\nWelcome to the Dice_Game!")
    bet=int(input("Place your bet: "))

    choice=int(input("Choose your lucky number(1-6): "))
    roll_dice=random.randint(1,6)
    
    print(f"the dice roll is: {roll_dice}")

    if bet> 100:
           print("You cannot bet more than your balance!")
           bet=int(input("Place again your bet: "))

    if choice == roll_dice:
        print("Congratulation!You won!")
        balance +=bet
    else:
        print("Sorry!You lost this round.")
        balance -=bet

    print(f"Your update balance: {balance}")

    

    if balance<=0:
        print("You balance is zero!")
        balance=int(input("How much do you buy?: "))
        print(f"Your update balance: {balance}")



    play_agin=input("Do you want to play again?(yes/no: )")
    if play_agin =='no' or play_agin == 'not':
        break
    else:
        continue










            
           
