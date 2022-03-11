import random
from _vendor.termcolor import colored
from time import sleep
with open("wordle-list.txt") as file:
    words = file.read().split("\n")

playing = True
pydleText1 = colored("Welcome to ", "green")
pydleText2 = colored("pydle", "magenta")
pydleText3 = colored("!", "green")
print("\n---------------------\n" + pydleText1 + pydleText2 + pydleText3 +
      "\n\nWordle, but in the terminal!\n---------------------\n\n")
sleep(1)
print('What color scheme would you like to use?\nLeave blank to use the default, and enter "custom" to choose any colors.')
colorScheme = input("Color scheme: ")
if colorScheme == "":
    colorScheme = "wordle"
outline = False  # Does not work when set to true
if colorScheme == "pydle":
    colorCorrect = "green"
    colorInWord = "magenta"
    colorNone = ""
elif colorScheme == "wordle" or colorScheme == "":
    colorCorrect = "green"
    colorInWord = "yellow"
    colorNone = ""
elif colorScheme == "alt":
    colorCorrect = "cyan"
    colorInWord = "blue"
    colorNone = "white"
elif colorScheme == "warm":
    colorCorrect = "yellow"
    colorInWord = "magenta"
    colorNone = "red"
elif colorScheme == "cold":
    colorCorrect = "blue"
    colorInWord = "cyan"
    colorNone = "magenta"
elif colorScheme == "simple":
    colorCorrect = "white"
    colorInWord = "cyan"
    colorNone = ""
elif colorScheme == "neon":
    colorCorrect = "magenta"
    colorInWord = "green"
    colorNone = "cyan"
elif colorScheme == "yellow":
    colorCorrect = "red"
    colorInWord = "white"
    colorNone = "yellow"
elif colorScheme == "hardMode":
    colorCorrect = "red"
    colorInWord = "red"
    colorNone = ""
elif colorScheme == "custom":
    print("Valid colors: grey, red, green, yellow, blue, magenta, cyan, and white.\nYou will get an error if you do not enter any of these colors exactly.\n")
    colorCorrect = input("Color when the letter is in the correct spot: ")
    colorInWord = input(
        "Color when the letter is in the word but in the wrong spot: ")
    colorNone = input(
        "Color when the letter is not in the word: ")
print("\nHow many letters do you want to play with? 5 is recommended.\n")
letterAmount = input("Number of letters: ")
letterAmount = int(letterAmount)
if letterAmount == 2:
    guessAmount = 2
elif letterAmount == 3:
    guessAmount = 3
elif letterAmount == 4:
    guessAmount = 4
elif letterAmount == 5:
    guessAmount = 6
elif letterAmount == 6:
    guessAmount = 8
elif letterAmount == 7:
    guessAmount = 15
elif letterAmount == 8:
    guessAmount = 26
else:
    print("\n\n\n\n\n\nThe number of letters should be from 2-8, but the game will still work with any positive integer.\n")
    guessAmount = 99
    # sleep(1)
if letterAmount != 5:
    warningText = colored("WARNING!", "red")
    print("\n!!!\n" + warningText + "\nThe answer list only applies to 5 letter words, so with any other number you can guess any word. Please be honorable and only guess valid english words.\n!!!\n")
    # sleep(3)
print("\nBased on the amount of letters, you will get " +
      str(guessAmount) + " guesses.\n")
sleep(3)
useless = input("Press enter to start.")

if outline:
    colorCorrect = "on_" + str(colorCorrect)
    colorInWord = "on_" + str(colorInWord)

while playing:
    # answer = random.choice(words)
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
        insertSpace()
        fullOutput.append(out)
        for item in fullOutput:
            print(item)

    def insertSpace():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    def update(out):
        # fullOutput[-1:] = out
        for item in fullOutput:
            insertSpace()
            print(item)
            sleep(0.2)

    for guessNum in range(guessAmount):
        guess = input("Guess #" + str(guessNum + 1) + ": ").strip()
        outList = []
        output = ""
        # latest = ""
        if letterAmount == 5:
            answerListLocation = "words"
        else:
            answerListLocation = None
        if answerListLocation == "words":
            if len(guess) == letterAmount and guess in words:
                validWord = True
            else:
                validWord = False
        elif answerListLocation == None:
            if len(guess) == letterAmount:
                validWord = True
            else:
                validWord = False

        if validWord:
            for i in range(letterAmount):
                if guess[i] == answer[i]:
                    #output += colored(guess[i], "green")
                    outList.append("#")
                    # latest = colored(guess[i], "green")
                    emojis += "🟩"
                elif guess[i] in answer:
                    #output += colored(guess[i], "yellow")
                    # latest = colored(guess[i], "yellow")
                    emojis += "🟨"
                    outList.append("-")
                else:
                    #output += guess[i]
                    outList.append("-")
                    # latest = colored(guess[i], "white")
                    emojis += "⬛️"
            outList2 = []
            for symbol, letter in zip(outList, guess):
                if symbol == "-":
                    countInGuess = 0
                    for symbol3, letter3 in zip(outList2, guess):
                        if symbol3 == "*" and letter3 == letter:
                            countInGuess += 1
                    countInAnswer = 0
                    for letter2, symbol2 in zip(answer, outList):
                        if letter2 == letter and not symbol2 == "#":
                            countInAnswer += 1
                    if countInAnswer > countInGuess:
                        outList2.append("*")
                    else:
                        outList2.append("-")
                else:
                    outList2.append("#")
            output = ""
            print(outList2)
            for letter, symbol in zip(guess, outList2):
                if symbol == "#":
                    if not outline:
                        output += colored(letter, colorCorrect)
                    else:
                        output += colored(letter, white, colorCorrect)
                if symbol == "*":
                    if not outline:
                        output += colored(letter, colorInWord)
                    else:
                        output += colored(letter, white, colorInWord)
                if symbol == "-":
                    if colorNone == "":
                        output += letter
                    else:
                        output += colored(letter, colorNone)

                insertSpace()
                print(output)
                sleep(0.3)
            # update(output)
            insertSpace()
            coolerPrint(output)
            emojis += "\n"
            if str(guess).strip() == str(answer).strip():
                print("Congrats! You got the word in " +
                      str(guessNum + 1) + " guesses!")
                break
        else:
            if len(guess) == letterAmount:
                coolerPrint("Not a valid word.")
            else:
                print("It's supposed to be " + letterAmount + " letters, not " +
                      str(len(guess)) + ".")
                # playing = False
                # break
    if not str(guess).strip() == str(answer).strip():
        print("The word was " + answer + "!")
        sleep(0.5)
    print("Your result: \n")
    print("pydle " + str(wordNum) + " " +
          str(guessNum + 1) + "/" + letterAmount)
    print(emojis)
    print("\n")
    ask = input("Press enter to play again, type anything to quit. ")
    if "" == ask:
        playing = False
    else:
        playing = True
