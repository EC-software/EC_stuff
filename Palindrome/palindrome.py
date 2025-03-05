
import pprint

def bit(n, b):
    """ take two int
    n: an int number, interpreted ad decimal, to be converted
    b: the bit-mode to convert to, e.g. 2 is binary, 16 is hex, etc.
    Return string representation of int n converted to 'b' bit system """
    # List of characters for bases higher than 10
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if n == 0:
        return '0'
    if b > 255:  # Edge case: base greater than 255
        raise ValueError("Base must be between 2 and 255.")
    result = []  # Result string, start from the least significant digit
    while n > 0:  # Convert n to base b
        result.append(digits[n % b])  # Append the current digit
        n //= b  # Reduce n by dividing by b
    return ''.join(reversed(result))  # Reverse the list to get the correct number in base b




def str_is_palindrome(str_in):
    """ Check if a string is a Palindrome
    Return True if it is, otherwise False. Empty string, and single letter strings are considered True. """
    # print(str_in)
    for n in range(round(len(str_in) / 2)):
        # print(f"{n}, {str_in} > {str_in[n]}, {str_in[-n-1]}")
        if str_in[n] != str_in[-n-1]:
            return False
    return True


def int_is_palindrome(int_in):
    return str_is_palindrome(str(int_in))


def main():

    # # Test examples
    # print(bit(33, 2))  # Output: '100001'
    # print(bit(33, 16))  # Output: '21'
    # print(bit(33, 8))  # Output: '41' (octal)
    # print(bit(255, 16))  # Output: 'FF' (hexadecimal)
    # print(bit(33, 62))  # Output: '53' (base 62, using digits and letters)

    # str_is_palindrome(3)
    # print(str_is_palindrome("abcdefgh"))
    # print(str_is_palindrome("b"))
    # print(str_is_palindrome("ml"))
    # print(str_is_palindrome("bab"))
    # print(str_is_palindrome("abba"))
    # print(str_is_palindrome("dfgh"))
    # print(str_is_palindrome("uytre"))
    # print(str_is_palindrome("12321"))
    # print(int_is_palindrome(12321))
    # print(int_is_palindrome(12345))

    dic_topscore = dict()
    for n in range(1000000000):
        if n > 9:  # Single digit are trivial Palindromes, and not interesting.
            if int_is_palindrome(n):
                dic_topscore[n] = {'10': str(n)}
                # print(f"decimal Palindrome: {n}")
                for b in range(2, 63):
                    if b != 10:  # We already tested decimal
                        nbitb = bit(n, b)
                        if len(nbitb) > 1 and str_is_palindrome(nbitb):  # Single digit are trivial Palindromes
                            dic_topscore[n][str(b)] = str(nbitb)
                            print(f"{n} base-{b} Palindrome: {nbitb}")
    # pprint.pprint(dic_topscore)
    print("\nTop-Scores")
    for k in sorted(dic_topscore.keys()):
        if len(dic_topscore[k]) > 5:
            print(f"DecPal: {k} ({len(dic_topscore[k])}) : {dic_topscore[k]}")

if __name__ == "__main__":

    main()