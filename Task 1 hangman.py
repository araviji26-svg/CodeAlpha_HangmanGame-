import random
word_list = ["python", "programming", "developer", "computer", "algorithm", "sequence"]
secret_word = random.choice(word_list)
word_display = ["_"] * len(secret_word)
attempts_left = 6
guessed_letters = []  
print("Welcome to Hangman!")
print("Word to guess: " + " ".join(word_display))
while attempts_left > 0 and "_" in word_display:
    print(f"\nAttempts remaining: {attempts_left}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single alphabetical letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one!")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts_left -= 1 
    print("Current progress: " + " ".join(word_display))
if "_" not in word_display:
    print("\n🎉 Congratulations! You guessed the word and won the game!")
else:
    print(f"\n💀 Game Over! You ran out of attempts. The word was: '{secret_word}'")
