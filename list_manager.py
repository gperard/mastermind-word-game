"""A class that represents a manager of the word list"""
from os.path import exists
import random
import json
import itertools


class ListManager:
    """Create and display list from text file"""

    def __init__(self, file, num_of_letters, num_of_words):
        """Initialize the attributes of the listManager"""
        self.word_list = []
        self.num_of_letters = num_of_letters
        self.num_of_words = num_of_words
        self.original_text_file = file
        self.unordered_list = str
        self.sorted_list = 'sorted_word_list.json'
        self.max_length = int

    def get_file(self):
        """Get txt file and create unordered list from contents"""
        try:
            with open(self.original_text_file, mode='r') as file_1:
                self.unordered_list = file_1.read().split()
        except FileNotFoundError:
            print('Your file does not exist.')
        else:
            return self.unordered_list

    def create_sorted_list(self):
        """Return a list of words (of a specific length) from a JSON file -by either creating a new file or
           accessing the existing one"""
        file_exists = exists(self.sorted_list)

        if file_exists is False:
            self.get_file()

            # Create JSON file with sorted/grouped word lists
            with open(self.sorted_list, mode='w') as file_2:
                grouped_list = itertools.groupby(self.unordered_list, key=len)
                new_data = {length_of_words: list(words) for length_of_words, words in grouped_list}
                self.max_length = len(new_data)
                json.dump(new_data, file_2)

        # Get list of words from local JSON file
        f = open(self.sorted_list)
        data = json.load(f)
        f.close()

        self.word_list = random.sample(data[str(self.num_of_letters)], self.num_of_words)
        return self.word_list

    def display_list(self):
        """Display the list of words"""
        print('Word List:')
        for word in self.word_list:
            print(word)