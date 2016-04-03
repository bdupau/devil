__author__ = 'Bastiaan'

from random import uniform


class Vowel:
    def __init__(self):
        busy = True
        while busy:
            self._backness = uniform(0.0, 1.0)
            self._openness = uniform(0.0, 1.0)
            if (self._backness  > self._openness / 2) & (1 - self._backness > self._openness / 2):
                busy = False

    def __str__(self):
        return str(round(self._backness, 2)) + " " + str(round(self._openness, 2))

    def get_backness(self):
        return self._backness

    def get_openness(self):
        return self._openness

    def distance_to(self, vowel):
        dif_backness = (self._backness - vowel.get_backness())**2
        dif_openness = (self._openness - vowel.get_openness())**2
        return dif_backness + dif_openness