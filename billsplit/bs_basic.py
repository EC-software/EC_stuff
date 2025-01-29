DIGITS = 0
EQUALSPLIT = True

def move2clear(dic_b, dic_c=dict()):
    """ Move all cleared accounts to dic_clear. """
    for key_a in dic_balance:  #
        if dic_b[key_a]['balnc'] == 0:
            dic_c[key_a] = dic_b[key_a]
    for key_a in dic_c:
        if key_a in dic_b.keys():
            del dic_b[key_a]
    return dic_b, dic_c

lot_expns = [('Bjørn', 150), ('Jakob', 3 * 125), ('Martin', 175)]  # What you did actually pay, i.e. the bills you picked up
print(f"Expendeces: {lot_expns}")

if EQUALSPLIT:
    num_ways = len(lot_expns)
    num_totexpend = sum([itm[1] for itm in lot_expns])
    print(f"Total expence: {num_totexpend} split: {num_ways} ways")
    lot_consu = [(itm[0], round((num_totexpend / num_ways), DIGITS)) for itm in lot_expns]  # What you should pay for, i.e. what you had to drink
else:
    lot_consu = []
print(f"Consumed: {lot_consu}")

dic_balance = {key_w:  {
    'expnd': [exp[1] for exp in lot_expns if exp[0] == key_w][0],
    'consu': [own[1] for own in lot_consu if own[0] == key_w][0],
    'balnc': round(([own[1] for own in lot_consu if own[0] == key_w][0] - [exp[1] for exp in lot_expns if exp[0] == key_w][0]), DIGITS)
    }
    for key_w in [itm[0] for itm in lot_expns]}
# # print(f"Ows: {dic_balance}")

# allocate the rounding error
num_rounderror = sum([dic_balance[key_a]['balnc'] for key_a in dic_balance.keys()])
if num_rounderror != 0.0:
    biggest = sorted([(abs(dic_balance[key_a]['balnc']), key_a) for key_a in dic_balance.keys()])[-1][1]
    print(f"Adjusting rounding error of {num_rounderror} at {biggest}")
    dic_balance[biggest]['balnc'] -= num_rounderror
# for key_a in dic_balance.keys():
#     dic_balance[key_a]['balnc'] = round(dic_balance[key_a]['balnc'], DIGITS)

dic_balance, dic_clear = move2clear(dic_balance)
print(f"Ows: {dic_balance}, Clr: {dic_clear}")

while len(dic_balance.keys()) > 0:
    lst_low = sorted([(dic_balance[key_a]['balnc'], key_a) for key_a in dic_balance.keys()])
    btm, top = lst_low[0], lst_low[-1]
    if top[0] > (-1 * btm[0]):  # top have more money than butm needs
        transf = (-1 * btm[0])  # only transfer part of Top's money
    else:
        transf = top[0]  # transfer all top's money
    print(f" * {top[1]} -> {btm[1]} : {transf}")
    dic_balance[top[1]]['balnc'] -= transf
    dic_balance[btm[1]]['balnc'] += transf
    dic_balance, dic_clear = move2clear(dic_balance, dic_clear)

