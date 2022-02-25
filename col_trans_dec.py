import ciphers

def col_trans_dec(code, key):
    decode = {}
    txt_length = len(code)
    key_length = len(key)
    extras = txt_length % key_length
    total_rows = -(txt_length // -key_length)
    counter = 0
    for x in key:
        if x < extras:
            rows = total_rows
        else:
            rows = 1
        for y in range(rows):
            pos = x + (key_length * y)
            if counter < txt_length:
                decode[pos] = code[counter]
                counter += 1

    return "".join([val for k, val in sorted(decode.items(), key=lambda e: e[0])])

# print(ciphers.col_trans("ANDYISTHEBEST"))
# print(col_trans_dec('dthbaetseynsi', [2, 7, 9, 0, 6, 5, 8, 3, 1, 4]))

# print(ciphers.col_trans("ILikePizza"))
print(col_trans_dec('izzkilpeia', [6, 8, 7, 3, 2, 1, 5, 4, 0]))