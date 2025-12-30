
import hashlib
import random

# Crockford's Base32 alphabet (URL-safe, excludes I, L, O, U)
CROCKFORD_ALPHABET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
# URL-safe separator character, for human readability
SEPARATOR_CHAR = '-'  # URL-safe char for separator (- also used for check-sum)
# URL-safe checksum characters
CHECKSUM_CHARS = '-._~'  # URL-safe chars for checksum (- also used for readability, Consider I, L, O, U)

def to_crockford_base32(number, length=None, hyphenate=False, checksum=False):
    """ Convert a number to Crockford's Base32. """
    if length is None:
        length = (number.bit_length() + 4) // 5
    result = []
    for _ in range(length):
        number, rem = divmod(number, 32)
        result.insert(0, CROCKFORD_ALPHABET[rem])  # Prepend, not append, as reminders are collected backwards
    if checksum:
        checksum_val = sum(CROCKFORD_ALPHABET.index(c) for c in result) % len(CHECKSUM_CHARS)
        result.append(CHECKSUM_CHARS[checksum_val])
    if hyphenate:
        result_str = ''.join(result)
        chunks = [result_str[i:i+4] for i in range(0, len(result_str), 4)]
        return SEPARATOR_CHAR.join(chunks)
    return ''.join(result)


def string_to_crockford_base32(input_str, length=8, hyphenate=False, checksum=False):
    """ Convert an input string to a Crockford's Base32 ID. """
    hash_int = int(hashlib.sha256(input_str.encode()).hexdigest(), 16)
    return to_crockford_base32(hash_int, length, hyphenate, checksum)

def random_crockford_base32(length=8, hyphenate=False, checksum=False):
    """ Generate a random Crockford's Base32 ID. """
    rand_int = random.getrandbits(length * 5)  # 5 bits per character
    return to_crockford_base32(rand_int, length, hyphenate, checksum)

# Example usage

# for n in range(8):
#     m = n+1
#     print(f"n: {m}; {32 ** m}")

num_len = 4
print(string_to_crockford_base32("Hello World!", length=num_len, hyphenate=True, checksum=True))
print(string_to_crockford_base32("Hello World!", length=num_len, hyphenate=False, checksum=True))
print(string_to_crockford_base32("Hello World!", length=num_len, hyphenate=True, checksum=False))
print(string_to_crockford_base32("Hello World!", length=num_len, hyphenate=False, checksum=False))

print(random_crockford_base32(length=8, hyphenate=True, checksum=False))
print(random_crockford_base32(length=8, hyphenate=False, checksum=True))
