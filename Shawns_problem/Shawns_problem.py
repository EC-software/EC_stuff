
import itertools
combinations = itertools.permutations(range(1, 13))
for combo in combinations:
    a = sum(combo[0:4])
    b = sum(combo[3:7])
    c = sum(combo[6:10])
    d = sum(combo[9:12]) + combo[0]
    if a == 25 and b == 25 and c == 25 and d == 25:
        print(f"Good: {combo} ; {combo[0:4]}, {combo[3:7]}, {combo[6:10]}, {combo[9:12]}+{combo[0]}")
