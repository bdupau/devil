__author__ = 'Bastiaan'

from lexical_element import LexicalElement
from vowel import Vowel
from random import randint


class Agent:
    def __init__(self, name):
        self._name = name
        self._lexicon = []

    def __str__(self):
        return self._name

    def print_lexicon(self):
        lexicon_string = ''
        for element in self._lexicon:
            lexicon_string += str(element) + '\n'
        print(lexicon_string)

    def _in_lexicon(self, topic):
        for element in self._lexicon:
            if element.get_topic() == topic:
                return True
        return False

    def _get_vowel_for(self, topic):
        elements = []
        for element in self._lexicon:
            if element.get_topic() == topic:
                elements.append(element)

        # this needs to be weighed:
        pick = randint(0, len(elements) - 1)

        element = elements[pick]
        self._memory = element
        return element.get_vowel()

    def _get_topic_for(self, vowel):
        match = 0
        highscore = 1
        for element in self._lexicon:
            score = vowel.distance_to(element.get_vowel())
            if score < highscore:
                highscore = score
                self._memory = element
                match = element.get_topic()
        return match

    def _utter(self, topic):
        if self._in_lexicon(topic):
            return self._get_vowel_for(topic)
        else:
            vowel = Vowel()
            element = LexicalElement(vowel, topic)
            self._lexicon.append(element)
            self._memory = element
            return vowel

    def interpret(self, vowel):
        guess = 0
        if len(self._lexicon) == 0:
            guess = randint(0, 2)
            element = LexicalElement(vowel, guess)
            self._lexicon.append(element)
            self._memory = element
        else:
            guess = self._get_topic_for(vowel)
        return guess

    def reinforce(self):
        self._memory.reinforce()

    def learn(self, vowel, topic):
        element = LexicalElement(vowel, topic)
        self._lexicon.append(element)

    def forget(self):
        for element in self._lexicon:
            element.forget()
            if element.get_weight() <= 0:
                self._lexicon.remove(element)

    def talk (self, partner):
        topic = randint(0,2)
        utterance = self._utter(topic)
        guess = partner.interpret(utterance)
        if guess == topic:
            self.reinforce()
            partner.reinforce()
        else:
            partner.learn(utterance, topic)
        self.forget()
        partner.forget()

        #print(str(self) + ' says ' + str(utterance) + ' for ' + str(topic))
        #print(str(partner) + ' guesses ' + str(guess))

john = Agent('John')
mary = Agent('Mary')
for i in range(1,50):
    john.talk(mary)
print("John:")
john.print_lexicon()
print("Mary:")
mary.print_lexicon()