# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word: str):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_' * len(word)
        self.guesses: list = []

    def guess(self, char: str):
        if self.status != STATUS_ONGOING:
            raise ValueError(f"The game has ended. You {self.status}.")
        self._update_remaining_guesses(char)
        self._update_masked_word(char)
        self._update_status()

    def _update_masked_word(self, char: str):
        masked_chars = list(self.masked_word)
        hits = [i for i, c in enumerate(self.word) if c == char]
        for hit in hits:
            masked_chars[hit] = char
        self.masked_word = ''.join(masked_chars)

    def _update_remaining_guesses(self, char: str):
        if char not in self.word or char in self.guesses:
            self.remaining_guesses -= 1
        else:
            self.guesses.append(char)

    def _update_status(self):
        if self.masked_word == self.word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        return self.masked_word

    def get_status(self) -> str:
        return self.status
