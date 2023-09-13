CIPHER: str = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI"
N: int = 26

def frequency_analysis(cipher: str) -> dict:
    # Calculating frequencies
    return dict(sorted({c: cipher.count(c) for c in cipher}.items(), key=lambda x:x[1], reverse=True))
    

def find_key(cipher: str) -> (int, int):
    # Finding the frequency of each letter in the cipher
    frequencies: dict = frequency_analysis(cipher)

    # Defining y1 to be the most frequent, and y2 to be the second most frequent
    y1: str = list(frequencies)[0] # C (32 occurrences)
    y2: str = list(frequencies)[1] # B (21 occurrences)

    # Converting to integers in range [0, 25]
    y1_int: int = ord(y1) - 65 # 2
    y2_int: int = ord(y2) - 65 # 1

    # Defining x1 and x2 as most frequent letters, based on table 4.1 in book
    x1: str = "E"
    x2: str = "T"

    # Converting to integers in range [0, 25]
    x1_int: int = ord(x1) - 65 # 4
    x2_int: int = ord(x2) - 65 # 19

    # Calculating a and b as described in chapter 4.4.1
    a: int = (y2_int - y1_int)*pow(x2_int-x1_int, -1, N) % N # 19
    b: int = (y1_int - a * x1_int) % N # 4

    return a, b

def affine(cipher: str) -> str:
    # getting keys
    a, b = find_key(cipher)

    # Decrypting ciphertext based on chapter 4.4.1
    return "".join([chr(pow(a, -1, N) * (ord(y) - 65 -b) % N + 65) for y in cipher])

print(affine(CIPHER))