from random import choices
from string import ascii_uppercase, digits


class Robot:
    def __init__(self):
        # When robots come off the factory floor, they have no name.
        self._name = None
        self._past_names = set()

    @property
    def name(self):
        if self._name is None:
            while True:
                self._name = self.random_name()
                if self._name not in self._past_names:
                    self._past_names.add(self._name)
                    break
        return self._name

    def reset(self):
        """Reset robot to its factory settings."""
        self._name = None

    @staticmethod
    def random_name():
        # Two random uppercase letters followed by three random digits
        return ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
