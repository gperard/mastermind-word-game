import random

"""A class used to represent the logic of the game """


class GameBrain:
    """Compare the words selected by the user with the secret word and give feedback"""

    def __init__(self, words, guesses):
        """Initialize attributes of the game brain"""
        self.words = words
        self.num_guesses = guesses
        self.secret_word = str
        self.user_word = str
        self.num_letters_correct = int
        self.answer = str

    def game_intro(self):
        """Print an introduction to the game to the user"""
        print(f'Welcome to Mastermind!!\nYour goal is to find the "secret" word from the list.')
        print('\t(type "q" or Ctrl-c to quit.)\n')
        print(f'Pick a word, but you only have {self.num_guesses} guesses: \n')

    def get_user_word(self):
        """Get the user's word(s)"""
        self.user_word = input(f'\nGuess ({self.num_guesses} left)? \n $ ').lower()
        self.num_guesses -= 1
        return self.user_word

    def get_secret_word(self):
        """Select a secret word for game play"""
        # random.seed(42)  # For testing -keep the same word list
        self.secret_word = random.choice(self.words)
        # print(f'\t***{self.secret_word}***')  # For testing -reveal the secret word

    def check_word(self, word_list):
        """Check if word is in word list. Return none if user quits, true if word is in wordlist and false if not"""
        if self.user_word == 'q':
            print("Quit game.")
            return 'q'
        elif self.user_word not in word_list:
            print("That word was not on the list. Lose a guess.")
            return False
        else:
            return True

    def compare_words(self):
        """Compare the user's word(s) with the secret word"""
        secret_word_dict = {key: value for key, value in enumerate(self.secret_word)}
        user_word_dict: dict = {key: value for key, value in enumerate(self.user_word)}

        shared_items = {}

        for keys in secret_word_dict:
            if secret_word_dict[keys] == user_word_dict[keys]:
                shared_items[keys] = user_word_dict[keys]

        self.num_letters_correct = len(shared_items)

    def give_feedback(self, word_from_list):
        """Give feedback to the user on game progress"""
        if word_from_list:
            print(f'{self.num_letters_correct}/{len(self.secret_word)} letters are correct')

        if self.num_letters_correct == len(self.secret_word):
            print('You win!')
            return False
        elif self.num_guesses == 0:
            print(f'Sorry! The secret word was -- {self.secret_word}.')
            return False
        return True

    def get_user_feedback(self):
        """Get user feedback to start a new game."""
        self.answer = input('\nWould you like to play another game? y or n: ').lower()
        return self.answer
