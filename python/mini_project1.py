import random

words = ["apple", "banana", "orange", "grape", "lemon"]

hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |  / \\
     |
    ---""",
    """
     ------
     |    |
     |    O
     |  ./|\\
     |  ./ \\.
     |
    ---""",
    """
     ------
     |    |
     |    O
     |  ./|\\
     |  ./ \\.
     |
    ---""",
    """
     ------
     |    |
     |    O
     |  ./|\\.
     |  ./ \\.
     |
    ---""",
]

class HangmanGame:
    def __init__(self):
        self.word = random.choice(words)
        self.guesses = set()
        self.attempts = len(hangman_pics) - 1

    def display(self):
        char = " "
        for i in self.word:
            if i in self.guesses:
                char += i
            else:
                char += "_ "
        return char

    def play(self):
        while self.attempts > 0:
            print(hangman_pics[len(hangman_pics) - self.attempts-1])
            print(self.display())
            print(f"Used letters: {', '.join(self.guesses)}")
            
            guess = input("글자를 추측해보세요: ").lower()

            if guess in self.guesses:
                print("You've already guessed that letter. Try another one.")
            elif guess in self.word:
                self.guesses.add(guess)
                if set(self.word) <= self.guesses:
                    print(f"Congratulations! You've guessed the word: {self.word}")
                    break
            else:
                self.attempts -= 1
                print(f"Wrong guess! Attempts left: {self.attempts}")

        if self.attempts == 0:
            print(hangman_pics[-1])
            print(f"Game over! The word was: {self.word}")

game = HangmanGame()
game.play()