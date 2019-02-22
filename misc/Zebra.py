import itertools

"""
 1) There are five houses in a row. They each have different colors, they each have a resident of a different nationality, they each listen to different kinds of music, drink different drinks, and each have a different kind of pet.
 2) The Englishman lives in the red house. *
 3) The Swede has a dog. *
 4) The person who lives in the green house drinks coffee. *
 5) The man who listens to classical music lives next to the house with the cat. *
 6) The Dane drinks tea. *
 7) The green house lies just to the right of the white house. *
 8) The lady who listens to rock music has a bird. *
 9) The person in the yellow house listens to jazz music. *
10) The person in the house in the middle drinks milk. *
11) The Norwegian lives in the house on the far left.  *
12) The person who listens to jazz music lives next to the person who has a horse.
13) The man who listens to pop music drinks beer. *
14) The German listens to country music. *
15) The Norwegian lives next to the blue house. *
16) The person who drinks water, lives next to the person who listen to classical music.
"""

colour = ['red', 'green', 'white', 'yellow', 'blue']
colours = [tup_col for tup_col in itertools.permutations(colour)]
nation = ['Eng', 'Swe', 'Dan', 'Nor', 'Ger']
nations = [tup_nat for tup_nat in itertools.permutations(nation)]
drink = ['coffee', 'tea', 'milk', 'beer', 'water']
drinks =  [tup_dri for tup_dri in itertools.permutations(drink)]
music = ['classic', 'rock', 'jazz', 'pop', 'country']
musics =  [tup_mus for tup_mus in itertools.permutations(music)]
pet = ['dog', 'cat', 'bird', 'horse', 'zebra']
pets = [tup_pet for tup_pet in itertools.permutations(pet)]

cnt = 0
for col in colours:
    for nat in nations:
        # 11) The Norwegian lives in the house on the far left.
        if nat[0] == 'Nor':
            # 15) The Norwegian lives next to the blue house.
            if col[1] == 'blue':
                # 2) The Englishman lives in the red house.
                if nat.index('Eng') == col.index('red'):
                    # 7) The green house lies just to the right of the white house.
                    if col.index('green') == (col.index('white') + 1):
                        for dri in drinks:
                            # 10) The person in the house in the middle drinks milk.
                            if dri[2] == 'milk':
                                # 4) The person who lives in the green house drinks coffee.
                                if col.index('green') == dri.index('coffee'):
                                    #  6) The Dane drinks tea.
                                    if nat.index('Dan') == dri.index('tea'):
                                        for mus in musics:
                                            # 9) The person in the yellow house listens to jazz music.
                                            if col.index('yellow') == mus.index('jazz'):
                                                # 13) The man who listens to pop music drinks beer.
                                                if mus.index('pop') == dri.index('beer'):
                                                    # 14) The German listens to country music.
                                                    if nat.index('Ger') == mus.index('country'):
                                                        for pez in pets:
                                                            #  3) The Swede has a dog.
                                                            if nat.index('Swe') == pez.index('dog'):
                                                                #  8) The lady who listens to rock music has a bird.
                                                                if mus.index('rock') == pez.index('bird'):
                                                                    #  5) The man who listens to classical music lives next to the house with the cat.
                                                                    if mus.index('classic') == (pez.index('cat') + 1) or mus.index('classic') == (pez.index('cat') - 1):
                                                                        # 12) The person who listens to jazz music lives next to the person who has a horse.
                                                                        if mus.index('jazz') == (pez.index('horse') + 1) or mus.index('jazz') == (pez.index('horse') - 1):
                                                                            # 16) The person who drinks water, lives next to the person who listen to classical music.
                                                                            # This question is obsolete, as we all ready have a fix.
                                                                            if dri.index('water') == (mus.index('classic') + 1) or dri.index('water') == (mus.index('classic') - 1):
                                                                                #print col, nat, dri, mus, pez
                                                                                cnt += 1
                                                                                print("The Zebra is owned by the: {}".format(nat[pez.index('zebra')]))


print("Number of valid solutions: {}".format(cnt))
