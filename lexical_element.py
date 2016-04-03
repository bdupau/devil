__author__ = 'Bastiaan'


class LexicalElement:
    def __init__(self, vowel, topic):
        self._vowel = vowel
        self._topic = topic
        self._weight = 0.1

    def __str__(self):
        return  str(self._vowel) + ": " + str(self._topic) + " (" + str(round(self._weight, 2)) + ")"

    def get_vowel(self):
        return self._vowel

    def get_topic(self):
        return self._topic

    def get_weight(self):
        return self._weight

    def reinforce(self):
        self._weight += 0.1
        if self._weight > 1:
            self._weight = 1.0

    def forget(self):
        self._weight -= 0.01
