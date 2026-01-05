import string

KEY = "MONARCHY"

def playfair_matrix():
    key = KEY.replace("J", "I")
    seen, mat = set(), []
    for c in key + string.ascii_uppercase:
        if c not in seen and c != 'J':
            seen.add(c)
            mat.append(c)
    return [mat[i:i+5] for i in range(0, 25, 5)]

def playfair_encrypt(msg):
    mat = playfair_matrix()
    pos = {mat[r][c]: (r, c) for r in range(5) for c in range(5)}
    msg = msg.upper().replace(" ", "").replace("J", "I")

    pairs, i = [], 0
    while i < len(msg):
        a = msg[i]
        b = msg[i+1] if i+1 < len(msg) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    cipher = ""
    for a, b in pairs:
        r1, c1 = pos[a]
        r2, c2 = pos[b]

        if r1 == r2:
            cipher += mat[r1][(c1 + 1) % 5] + mat[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += mat[(r1 + 1) % 5][c1] + mat[(r2 + 1) % 5][c2]
        else:
            cipher += mat[r1][c2] + mat[r2][c1]

    return cipher

def english_score(text):
    freq = "ETAOIN"
    return sum(text.count(c) for c in freq)

def playfair_analysis(cipher):
    return english_score(cipher)

# -------- MAIN --------
msg = input("Enter message: ")
cipher = playfair_encrypt(msg)

print("Encrypted:", cipher)
print("English-likeness score:", playfair_analysis(cipher))
