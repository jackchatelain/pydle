import random
from termcolor import colored
from time import sleep
with open("wordle-list.txt") as file:
    words = file.read().split("\n")
playing = True
while playing:
    #answer = random.choice(words)
    wordNum = random.randint(0, 12946)
    answer = words[wordNum]
    guessNum = 0
    fullOutput = []
    additionalOutput = ""
    emojis = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---start---\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def coolPrint(thing):
        for i in thing:
            print(i, end="")
            sleep(0.2)
        print("")

    def coolerPrint(out):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        fullOutput.append(out)
        for item in fullOutput:
            print(item)

    def update(out):
        #fullOutput[-1:] = out
        for item in fullOutput:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(item)
            sleep(0.2)

    for guessNum in range(6):
        guess = input("Guess #" + str(guessNum + 1) + ": ").strip()
        output = ""
        if len(guess) == 5 and guess in words:
            for i in range(5):
                if guess[i] == answer[i]:
                    output += colored(guess[i], "green")
                    emojis += "🟩"
                elif guess[i] in answer:
                    output += colored(guess[i], "yellow")
                    emojis += "🟨"
                else:
                    output += guess[i]
                    emojis += "⬛️"
                # update(output)
            coolerPrint(output)
            emojis += "\n"
            if str(guess).strip() == str(answer).strip():
                print("Congrats! You got the word in " +
                      str(guessNum + 1) + " guesses!")
                break
        else:
            if len(guess) == 5:
                coolerPrint("Not a valid word.")
            else:
                print("It's supposed to be five letters, not " +
                      str(len(guess)) + "!")
                #playing = False
                # break
    if not str(guess).strip() == str(answer).strip():
        print("The word was " + answer + "!")
        sleep(0.5)
    print("Your result: \n")
    print("pydle (Word #" + str(wordNum) + ")")
    print(emojis)
    print("\n")
    ask = input("Do you want to play again? ")
    if "ye" in ask:
        playing = True
    else:
        playing = False
