# Decode what polyalph produces
# Solution call decode, decode_with_spaces

def shiftBackBy(c, n):
    return chr(((ord(c) - ord('a') - n) % 26) + ord('a')).upper()

def decode(code, key):
    decode = []
    for i in range(len(code)):
        shift = key[i % len(key)]
        if shift > 0:
            letter = shiftBackBy(code[i], shift)
        else:
            letter = code[i]
        decode.append(letter)
    return "".join(decode)

# return "".join([shiftBackBy(code[i], key[i % len(key)]) for i in range(len(code))])

def decode_with_spaces(code, key):
    return decode(code.replace(' ', ''), key)

# raw = decode("tvcrqrmpdzzdtbdlb", [19, 8, 25])
# print("Raw 1 is: ", raw)
#
# raw = decode_with_spaces("ytgwo vrnhe xhyzh qz", [24, 6, 3])
# print("Raw without spaces is: ", raw)