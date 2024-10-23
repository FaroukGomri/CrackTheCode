import random
number = random.sample(range(10),4)
number = "".join(map(str,number))

print("You have to Crack the Code !")
print("The code contains 4 digits.")

attempts = 0

def guess(guess, number):
    output = ""
    for i in range(len(number)):
        if guess[i] == number[i]:
            output += f"\033[92m{guess[i]}\033[0m"
        elif guess[i] in number:
            output += f"\033[93m{guess[i]}\033[0m"
        else:
            output += guess[i]
    return output

while True:
    try:
        playerGuess = input("Guess the code : ")
        if len(playerGuess) != 4 or not playerGuess.isdigit():
            print("Enter a 4 digit code.")
            continue

    except ValueError:
        print("Enter a valid code!")
        continue

    attempts += 1

    print("Output : "+guess(playerGuess,number))

    if playerGuess == number:
        print(f"Congrats ! have Cracked the Code in {attempts} attempts !! ")
        break