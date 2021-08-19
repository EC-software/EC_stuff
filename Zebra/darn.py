

nat = {'a': 'English', 'b': 'Spanish', 'c': 'Ukraine', 'd': 'Norwegian', 'e': 'Japanese'}
col = {'a': 'red', 'b': 'green', 'c': 'ivory', 'd': 'yellow', 'e': 'blue'}
pet = {'a': 'dog', 'b': 'snails', 'c': 'fox', 'd': 'horse', 'e': 'zebra'}
dri = {'a': 'coffee', 'b': 'tea', 'c': 'milk', 'd': 'orange juice', 'e': 'water'}
smo = {'a': 'Old Gold', 'b': 'Kools', 'c': 'Chesterfields', 'd': 'Lucky strike', 'e': 'Parliaments'}

data = {
    'nat': ['', '', '', '', ''],
    'col': ['', '', '', '', ''],
    'pet': ['', '', '', '', ''],
    'dri': ['', '', '', '', ''],
    'smo': ['', '', '', '', '']}


def isit(d, w, n, c):
    """ like: The Norwegian lives in the first house."""
    return d[w][n] == c  # n = number, c = character


def pair(d, w1, c1, w2, c2):
    """ like: The Ukrainian drinks tea. """
    pos1 = d[w1].find(c1)  # w1 = nationality, c1 = Ukrainian
    pos2 = d[w2].find(c2)
    return pos1 >= 0 and pos1 == pos2


def imidrightof(d, w1, c1, w2, c2):
    """ like: The green house is immediately to the right of the ivory house. """
    pos1 = d[w1].find(c1)
    pos2 = d[w2].find(c2)
    return (pos1 >= 0 and pos2 >= 0) and pos1 == (pos2 + 1)


def nextto(d, w1, c1, w2, c2):
    """ like: The Norwegian lives next to the blue house. """
    pos1 = d[w1].find(c1)
    pos2 = d[w2].find(c2)
    return (pos1 >= 0 and pos2 >= 0) and (pos1 == (pos2 + 1) or pos1 == (pos2 - 1))


def valid(data):
    """ Check all requirements """