import random
uscore = 0
cscore = 0
play_again="yes"
choices = ['rock', 'paper', 'scissors']
def winner(user, comp):
    if user == comp:
        return "It's a tie!"
    elif (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper') or (user == 'paper' and comp == 'rock'):
        return "You win!"
    else:
        return "You lose!"

while play_again=="yes":
    print("\n--- Rock-Paper-Scissors Game ---")
    print("Choose one: rock, paper, or scissors")
    user = input("Your choice: ").lower()
    
    if user not in choices:
        print("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")
        continue
    comp = random.choice(choices)
    print("Computer chose: ", comp)
    result = winner(user, comp)
    print(result)

    if result == "You win!":
        uscore += 1
    elif result == "You lose!":
        cscore += 1

    print(f"Score - You:",uscore, "Computer: ",cscore)

    play_again = input("Do you want to play another round? (yes/no): ").lower()
else:
    print("Thanks for playing!")
