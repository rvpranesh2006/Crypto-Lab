import itertools

KEY = "4312567"

# ---------------- ENCRYPTION ----------------

def columnar_encrypt(message):
    message = message.upper().replace(" ", "")
    cols = len(KEY)
    rows = (len(message) + cols - 1) // cols

    matrix = [['X' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(message):
                matrix[r][c] = message[index]
                index += 1

    order = sorted(range(cols), key=lambda i: KEY[i])

    cipher = ""
    for c in order:
        for r in range(rows):
            cipher += matrix[r][c]

    return cipher


# ---------------- ENGLISH SCORING ----------------

def english_score(text):
    common_letters = "ETAOIN"
    score = 0
    for c in common_letters:
        score += text.count(c)
    return score


# ---------------- DECRYPT WITH PERMUTATION ----------------

def columnar_decrypt_with_perm(cipher, perm):
    key_len = len(perm)
    rows = len(cipher) // key_len

    matrix = [['' for _ in range(key_len)] for _ in range(rows)]

    index = 0
    for p in perm:
        for r in range(rows):
            matrix[r][p] = cipher[index]
            index += 1

    plaintext = ""
    for r in range(rows):
        for c in range(key_len):
            plaintext += matrix[r][c]

    return plaintext


# ---------------- CRYPTANALYSIS ----------------

def transposition_cryptanalysis(cipher):
    best_plain = ""
    best_score = -1

    for key_len in range(2, 9):
        if len(cipher) % key_len != 0:
            continue

        for perm in itertools.permutations(range(key_len)):
            plain = columnar_decrypt_with_perm(cipher, perm)
            score = english_score(plain)

            if score > best_score:
                best_score = score
                best_plain = plain

    return best_plain


# ---------------- MAIN ----------------

message = input("Enter message: ")

ciphertext = columnar_encrypt(message)
print("\nEncrypted:", ciphertext)

recovered_text = transposition_cryptanalysis(ciphertext)
print("Recovered Plaintext (analysis):", recovered_text)
