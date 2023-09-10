import random
from _vendor.termcolor import colored
from time import sleep
playing = True
pydleText1 = colored("Welcome to ", "green")
pydleText2 = colored("pydle", "magenta")
pydleText3 = colored("!", "green")
print("\n---------------------\n" + pydleText1 + pydleText2 + pydleText3 +
      "\n\nWordle, but in the terminal!\n---------------------\n\n")
sleep(1)
useless = input("Press enter to start, or type anything to change settings. ")
if useless != "":
    print('What color scheme would you like to use?\nLeave blank to use the default, enter "custom" to choose any colors, or enter "colorblind" for a red and blue theme.')
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
    elif colorScheme == "colorblind":
        colorCorrect = "blue"
        colorInWord = "red"
        colorNone = ""
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
    if colorScheme != "":
        if colorNone == "":
            colorNone = "white"
        print("Correct color - " + colored(colorCorrect, colorCorrect) + "\nIn word color - " +
              colored(colorInWord, colorInWord) + "\nIncorrect color - " + colored(colorNone, colorNone))
    print("\nHow many letters do you want to play with? 5 is recommended.\n")
    letterAmount = input("Number of letters: ")
    if letterAmount == "":
        letterAmount = 5
    letterAmount = int(letterAmount)
    if letterAmount == 1:
        guessAmount = 16
    if letterAmount == 2:
        guessAmount = 11
    elif letterAmount == 3:
        guessAmount = 8
    elif letterAmount == 4:
        guessAmount = 5
    elif letterAmount == 5:
        guessAmount = 6
    elif letterAmount == 6:
        guessAmount = 11
    elif letterAmount == 7:
        guessAmount = 13
    elif letterAmount == 8:
        guessAmount = 20
    elif letterAmount <= 25:
        guessAmount = 99
    else:
        print("\n\n\n\n\n\n\n")
        guessAmount = 99
        warningText = colored("WARNING!", "red")
        print("\n!!!\n" + warningText +
              "\npydle only works with word length in range 1-25.\n!!!\n")
        sleep(5)
        # sleep(3)
    print("\nBased on the amount of letters, you will get " +
          str(guessAmount) + " guesses.\n")
    #extraInfo = input("(Yes or no) Would you like to display extra info? ")
    extraInfo = False  # Has some problems
    # if "ye" in extraInfo or "True" in extraInfo:
    #    extraInfo = True
    # else:
    #    extraInfo = False
    delay = input(
        "How long do you want the delay between revealing the letters in milliseconds? Leave blank for auto. ")
    if delay == "":
        delay = "auto"
    # else:
    #     delay = int(delay)
    useless = input("\nPress enter to start.")
else:
    colorCorrect = "green"
    colorInWord = "yellow"
    colorNone = ""
    colorScheme = "wordle"
    guessAmount = 6
    letterAmount = 5
    outline = False
    extraInfo = False
    delay = "auto"
keyboard = "qwertyuiopasdfghjklzxcvbnm"
startKeyboard = "qwertyuiopasdfghjklzxcvbnm"
knownLetters = ""

if outline:
    colorCorrect = "on_" + str(colorCorrect)
    colorInWord = "on_" + str(colorInWord)


if letterAmount == 5:
    with open("wordle-list.txt") as file:
        words = file.read().split("\n")
else:
    filename = str(letterAmount) + "-list.txt"
    with open(filename) as file:
        words = file.read().split("\n")

while playing:
    # answer = random.choice(words)
    wordNum = random.randint(0, len(words) - 1)
    answer = words[wordNum]
    for character in answer:
        knownLetters += "-"
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
        if len(guess) == letterAmount and guess in words:
            for i in range(letterAmount):
                if guess[i] == answer[i]:
                    # output += colored(guess[i], "green")
                    outList.append("#")
                    # latest = colored(guess[i], "green")
                    emojis += "🟩"
                elif guess[i] in answer:
                    # output += colored(guess[i], "yellow")
                    # latest = colored(guess[i], "yellow")
                    emojis += "🟨"
                    outList.append("-")
                else:
                    # output += guess[i]
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
                        for letter4, letter5, letter6 in zip(knownLetters, guess, answer):
                            knownLetters = ""
                            if letter5 == letter6:
                                knownLetters += letter4
                            else:
                                knownLetters += "-"
                        for letter4, letter5, letter6, letter7 in zip(keyboard, guess, answer, startKeyboard):
                            keyboard = ""
                            if letter5 == letter6:
                                keyboard += colored(letter7, colorCorrect)
                            else:
                                keyboard += letter7
                    else:
                        output += colored(letter, white, colorCorrect)
                if symbol == "*":
                    if not outline:
                        output += colored(letter, colorInWord)
                    else:
                        output += colored(letter, white, colorInWord)
                    for letter4, letter5, letter6, letter7 in zip(keyboard, guess, answer, startKeyboard):
                        keyboard = ""
                        if letter5 == letter6:
                            keyboard += colored(letter7, colorInWord)
                        else:
                            keyboard += letter7
                if symbol == "-":
                    if colorNone == "":
                        output += letter
                    else:
                        if colorScheme == "" or colorScheme == "pydle":
                            output += str(letter)
                        else:
                            output += colored(letter, colorNone)

                insertSpace()
                print(output)
                # sleep(0.3)
                if delay == "auto":
                    sleep(1.5 / letterAmount)
                elif delay == 0:
                    pass
                else:
                    sleep(int(delay) / 1000)
            # update(output)
            insertSpace()
            coolerPrint(output)
            if extraInfo == True:
                print("\n" + keyboard)
                print("\n" + knownLetters)
            emojis += "\n"
            if str(guess).strip() == str(answer).strip():
                print("Congrats! You got the word in " +
                      str(guessNum + 1) + " guesses!")
                break
        else:
            if len(guess) == letterAmount:
                coolerPrint(str(guess) + " is not a valid word.")
                for guessCharacter in guess:
                    emojis += "🟥"
                emojis += "\n"
            else:
                print("Please enter a " + str(letterAmount) + " letter word, not a " +
                      str(len(guess)) + " letter word.")
                for guessCharacter in guess:
                    emojis += "🟥"
                emojis += "\n"
                # playing = False
                # break
    if not str(guess).strip() == str(answer).strip():
        print("The word was " + answer + "!")
        sleep(0.5)
    print("Your result: \n")
    print("pydle " + str(wordNum + 1) + " " +
          str(guessNum + 1) + "/" + str(guessAmount))
    print(emojis)
    ask = input("\nPress enter to play again, type anything to quit. ")
    if "" == ask:
        playing = True
    else:
        playing = False
