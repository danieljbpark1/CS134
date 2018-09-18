# A text-generating Oracle.
# (c) 2018 by daniel j. park
"""This file defines a class, Oracle, that can generate random readable
text based on a training text."""

from random import randint, choice

__all__ = ['Oracle']

class Oracle(object):
    """Oracle can scan a training text and generate random 'readable' text
    based on the training text."""
    __slots__ = [ 'w', 'd', 't' ]
    
    def __init__(self, window=8):
        """Initializes Oracle with a window value, a dictionary of fingerprints,
        and a training text."""
        self.w = window
        self.d = dict()
        self.t = ''

    def intern(self, text):
        """Takes a string, and records occurences of window-sized character combinations
        in dictionary with first w-1 characters of fingerprint as key and a string of all
        last characters as value."""
        l = len(text)
        wCount = l - self.w + 1
        for start in range(wCount):
            peek = text[start:start+self.w]
            front = peek[:-1]
            back = peek[-1]
            endings = self.d.get(front,'')
            self.d[front] = endings + back
        self.t += text

    def follows(self, s):
        """Takes a string at least w-1 characters long and returns a probable next character
        based on the training text."""
        assert (len(s)>=self.w-1),"Seed string must be at least w-1 characters long."
        s = s[-self.w+1:]
        if not self.d.get(s) is None:
            return (choice(self.d[s]))
        else:
            return (choice(self.t))

    def generate(self, seed, length=80):
        """Takes a seed and builds a new string 'length' long based on training text
        and prints new string."""
        while len(seed)<=length:
            seed+=self.follows(seed)
        print(seed)

if __name__ == "__main__":
    o = Oracle(window=7)
    text = ' '.join([line.strip() for line in open('tomsawyer.txt')])
    o.intern(text)
    o.generate('i want to ',length=80*50) 

