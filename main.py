from list_manager import ListManager
from game_brain import GameBrain

text_file = 'original_word_list.txt'
list_manager = ListManager(text_file, num_of_letters=7, num_of_words=10)

num_of_guesses = 4
game_active = True

while game_active:
    word_list = list_manager.create_sorted_list()
    mastermind = GameBrain(word_list, num_of_guesses)
    mastermind.game_intro()
    list_manager.display_list()
    mastermind.get_secret_word()

    for i in range(num_of_guesses):
        mastermind.get_user_word()
        in_list = mastermind.check_word(word_list)

        if in_list == 'q':
            game_active = False
            break
        elif in_list:
            mastermind.compare_words()
        continue_game = mastermind.give_feedback(in_list)

        if not continue_game:
            restart_game = mastermind.get_user_feedback()
            if restart_game != "y":
                game_active = False
            break
