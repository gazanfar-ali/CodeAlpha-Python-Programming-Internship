import random

words = ["python", "hangman", "programming", "developer"]

word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(word_to_guess))  

while attempts_left > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\n💀 Game Over! The word was:", word_to_guess)
