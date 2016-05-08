#Disable 'Enter' key while in the quiz


while True:
    import random

    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone", "Python", "Jumble", "Easy", "Difficult", "Answer", "Xylophone")
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print(
    """
          Welcome to WORD JUMBLE!!!
          Words are CaSE SENsiTiVE
          Unscramble the leters to make a word.
          (press the enter key at prompt to quit)
          """
          )
    print("The jumble is:", jumble)
    guess = input("Your guess: ")
    while guess != correct and guess != "":
        print("Sorry, that's not it")
        guess = input("Your guess: ")
    if guess == correct:
        print("That's it, you guessed it!\n")
    print("Thanks for playing")

    input("\n\nPress the 'Enter' key to play again!")
    
