import numpy as np


class Hangman:
    def __init__(self):
        self.dictionary = None
        self.guessed_word = None
        self.secret_word = None
        self.used_letters = ''

        self.load_dictionary()
        self.guess_word()
        self.construct_secret_word()

    def load_dictionary(self):
        words = []
        with open('hangman/dictionary.txt', 'r') as file:
            for line in file:
                words.append(line)
        self.dictionary = list(map(lambda x: x.strip().lower(), words))

    def guess_word(self):
        word = np.random.choice(self.dictionary)
        self.guessed_word = word

    def construct_secret_word(self):
        self.secret_word = []
        for _ in self.guessed_word:
            self.secret_word.append('*')

    def check_letter(self, letter):
        if letter in self.used_letters:
            return False, self.secret_word
        self.used_letters += letter
        if letter in self.guessed_word:
            ind = self._indexes(letter)
            for symb in ind:
                self.secret_word[symb] = letter
            return True, self.to_str(self.secret_word)
        return False, self.to_str(self.secret_word)

    @staticmethod
    def to_str(lst):
        return ''.join(lst)

    def _indexes(self, letter):
        indexes = [-1]
        while True:
            try:
                indexes.append(self.guessed_word.index(
                    letter, indexes[-1] + 1))
            except ValueError:
                break
        return indexes[1:]


class Player:
    def __init__(self):
        self.max_mistake = 5
        self.mistake_num = 0
        self.result = None
        self.word = None
        self.server = Hangman()

    def play(self):
        while True:
            letter = self.get_letter()
            if not letter:
                continue
            self.result, self.word = self.server.check_letter(letter)
            self.check_result()
            self._print_word()
            game_status = self._game_status_check()
            if not game_status:
                break

    @staticmethod
    def get_letter():
        letter = input('Guess a letter: ')
        if not letter.isalpha():
            return False
        if len(letter) != 1:
            return False
        letter = letter.lower()
        return letter

    def _print_word(self):
        print(f'The word: {self.word}\n')

    def check_result(self):
        if self.result:
            print('Hit!\n')
        else:
            self.mistake_num += 1
            print(f'Missed, mistake {self.mistake_num} out of 5.\n')

    def _game_status_check(self):
        if self.mistake_num < self.max_mistake and '*' in self.word:
            print()
            return True
        if self.mistake_num < self.max_mistake and '*' not in self.word:
            print('You won!')
            return False
        if self.mistake_num >= self.max_mistake:
            print('You lost!')
            return False


if __name__ == '__main__':
    Player().play()
