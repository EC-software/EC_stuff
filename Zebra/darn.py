import itertools

nat = {'a': 'English', 'b': 'Spanish', 'c': 'Ukraine', 'd': 'Norwegian', 'e': 'Japanese'}  # nationality
col = {'a': 'red', 'b': 'green', 'c': 'ivory', 'd': 'yellow', 'e': 'blue'}  # colour
pet = {'a': 'dog', 'b': 'snails', 'c': 'fox', 'd': 'horse', 'e': 'zebra'}  # pet animal
dri = {'a': 'coffee', 'b': 'tea', 'c': 'milk', 'd': 'orange juice', 'e': 'water'}  # drinks
smo = {'a': 'Old Gold', 'b': 'Kools', 'c': 'Chesterfields', 'd': 'Lucky strike', 'e': 'Parliaments'}  # smokes

data = {
    'nat': ['', '', '', '', ''],
    'col': ['', '', '', '', ''],
    'pet': ['', '', '', '', ''],
    'dri': ['', '', '', '', ''],
    'smo': ['', '', '', '', '']}


def isit(d, w, n, c):
    """ like: The Norwegian lives in the first house."""
    return d[w][n] == '' or d[w][n] ==  c  # n = number, c = character


def pair(d, w1, c1, w2, c2):
    """ like: The Ukrainian drinks tea. """
    if all([c != '' for c in data[w1]]):
        if all([c != '' for c in data[w2]]):
            pos1 = [n for n in range(5) if d[w1][n] == c1]  # w1 = nationality, c1 = Ukrainian
            pos2 = [n for n in range(5) if d[w2][n] == c2]
            return len(pos1) > 0 and len(pos2) > 0 and pos1[0] == pos2[0]
    return True  # If we can't test it it isn't a violation of the rule


def imidrightof(d, w1, c1, w2, c2):
    """ like: The green house is immediately to the right of the ivory house. """
    pos1 = d[w1].find(c1)
    pos2 = d[w2].find(c2)
    return (pos1 >= 0 and pos2 >= 0) and pos1 == (pos2 + 1)


def nextto(d, w1, c1, w2, c2):
    """ like: The Norwegian lives next to the blue house. """
    if all([c != '' for c in data[w1]]):
        if all([c != '' for c in data[w2]]):
            pos1 = [n for n in range(5) if d[w1][n] == c1]  # w1 = nationality, c1 = Ukrainian
            pos2 = [n for n in range(5) if d[w2][n] == c2]
            return (len(pos1) > 0 and len(pos2) > 0) and (pos1[0] == (pos2[0] + 1) or pos1[0] == (pos2[0] - 1))
    return True  # If we can't test it it isn't a violation of the rule


def valid(data):
    """ Check all requirements """
    if len(set(data['nat'])) == 5:
        if not isit(data, 'nat', 0, 'd'):  # The Norwegian lives in the first house.
            return False
        if not isit(data, 'dri', 2, 'c'):  # Milk is drunk in the middle house.
            return False
        if not nextto(data, 'nat', 'd', 'col', 'e'):  # The Norwegian lives next to the blue house
            return False
        # if not pair(data, "nat", "a", "col", "a"):  # The Englishman lives in the red house.
        #     return False
        return True
    else:
        return False

def main(data):
    for cmb_n in itertools.permutations('abcde'):
        data['nat'] = cmb_n
        if valid(data):
            for cmb_d in itertools.permutations('abcde'):
                data['dri'] = cmb_d
                if valid(data):
                    print(f"data: {data}")
                    for cmb_c in itertools.permutations('abcde'):
                        data['col'] = cmb_c
                    #     for cmb_p in itertools.permutations('abcde'):
                    #         data['pet'] = cmb_p
                    #         for cmb_s in itertools.permutations('abcde'):
                    #             data['smo'] = cmb_s
                    #             if valid(data):
                    #                 print(f"HIT!: {data}")


if __name__ == '__main__':
    main(data)
