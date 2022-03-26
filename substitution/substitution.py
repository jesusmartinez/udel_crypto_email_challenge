from EmailChallenge import fetch_email
from collections import Counter
from alg import decode

text = fetch_email.get_mail_2()
# print(text)

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
normal_freq_sorted = {k: val for k, val in sorted(normal_freqs.items(), key=lambda e: e[1], reverse=1)}
normal_bigram_freq = {'th': 0.03882543, 'he': 0.03681391, 'in': 0.02283899, 'er': 0.02178042, 'an': 0.02140460, 're': 0.01749394, 'nd': 0.01571977, 'on': 0.01418244, 'en': 0.01383239, 'at': 0.01335523, 'ou': 0.01285484, 'ed': 0.01275779, 'ha': 0.01274742, 'to': 0.01169655, 'or': 0.01151094, 'it': 0.01134891, 'is': 0.01109877, 'hi': 0.01092302, 'es': 0.01092301, 'ng': 0.01053385}
normal_trigram_freq = {'the': 0.03508232,'and': 0.01593878,'ing': 0.01147042,'her': 0.00822444,'hat': 0.00650715,'his': 0.00596748,'tha': 0.00593593,'ere': 0.00560594,'for': 0.00555372,'ent': 0.00530771,'ion': 0.00506454,'ter': 0.00461099,'was': 0.00460487,'you': 0.00437213,'ith': 0.00431250,'ver': 0.00430732,'all': 0.00422758,'wit': 0.00397290,'thi': 0.00394796,'tio': 0.00378058}

def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))
def analyse(text):
    freq = Counter(text[idx] for idx in range(len(text)))
    print("Total letters: " + str(len(freq)))
    freq_sorted = {k: val for k, val in sorted(freq.items(), key=lambda e: e[1], reverse=1)}
    print(str(freq_sorted))

    frequency = {}
    for l in freq_sorted:
        enc1 = text.count(l)
        frequency[l] = float(enc1) / len(text)
    print("Frequency", frequency)
    print("Normal Fr " + str(normal_freq_sorted))

    print("-----------------------------------")
    bigrams = Counter(text[idx: idx + 2] for idx in range(len(text) - 1))
    bigrams_sorted = {k: val for k, val in sorted(bigrams.items(), key=lambda e: e[1], reverse=1)}
    bigram_freq = {}
    for bi in bigrams_sorted:
        enc1 = text.count(bi)
        bigram_freq[bi] = float(enc1) / (len(bigrams))
    # print("Bigrams tot", str(dict(bigrams_sorted)))
    # print("Bigram Freq", str(dict(bigram_freq)))
    # print("Normal Freq", str(normal_bigram_freq))
    bi = [a for a, b in bigram_freq.items()]
    bi_n = [a.upper() for a, b in normal_bigram_freq.items()]
    print("Bigram Freq", str(bi))
    print("Normal Freq", str(bi_n))

    print("-----------------------------------")
    trigrams = Counter(text[idx: idx + 3] for idx in range(len(text) - 2))
    trigrams_sorted = {k: val for k, val in sorted(trigrams.items(), key=lambda e: e[1], reverse=1)}
    trigram_freq = {}
    for tri in trigrams_sorted:
        enc1 = text.count(tri)
        trigram_freq[tri] = float(enc1) / len(trigrams)
    # print("Trigram Freq", str(dict(trigram_freq)))
    # print("Normal  Freq", str(normal_trigram_freq))
    tri = [a for a, b in trigram_freq.items()]
    tri_n = [a.upper() for a, b in normal_trigram_freq.items()]
    print("Trigram Freq", str(tri))
    print("Normal  Freq", str(tri_n))

    # print("-----------------------------------")
    # print(check_top(normal_freqs, normal_bigram_freq, normal_trigram_freq))
    # print(check_top(frequency, bigram_freq, trigram_freq))

    # key = [-1 for i in range(26)]
    # key = swap(key, 'e', 'o')
    # view_key(key)
    # top = 8
    # tri = [a for a, b in trigram_freq.items()]
    # tri_n = [a for a, b in normal_trigram_freq.items()]
    # for i in range(top):
    #     print(tri[i], tri_n[i].upper())
    #     key = swap(key, tri_n[i], tri[i])
    #     view_key(key)
    # print(decode(text, key))
    #
    # bi = [a for a, b in bigram_freq.items()]
    # bi_n = [a for a, b in normal_bigram_freq.items()]
    # for i in range(top):
    #     print(bi[i], bi_n[i].upper())
    #     key = swap(key, bi_n[i], bi[i])
    #     view_key(key)
    # print(decode(text, key))


top = 10
def check_top(letters, bigrams, trigrams):
    matches_bi = []
    matches_tri = []
    both_matches = []
    g = [a for a, b in letters.items()]
    for letter in g[:top]:
        bi = [a for a, b in bigrams.items()]
        for bigram in bi[:top]:
            if letter in bigram and letter not in matches_bi:
               matches_bi.append(letter)
               both_matches.append(letter)
        tri = [a for a, b in trigrams.items()]
        for trigram in tri[:top]:
            if letter in trigram and letter not in matches_tri:
                matches_tri.append(letter)
                if letter not in both_matches:
                    both_matches.append(letter)

    return both_matches
    # return matches_bi, matches_tri

    # return a Key


    # found = 0
    # sum_sqr_frequencies = {}
    # for possible_key in range(1, 26):
    #     sum_f_sqr = 0.0
    #     for ltr in normal_freqs:
    #         caesar_guess = shiftBy(ltr, possible_key)
    #         if (frequency.get(caesar_guess) == None):
    #             continue
    #         sum_f_sqr += normal_freqs[ltr]*frequency[caesar_guess] # IMPORTANT
    #     if abs(sum_f_sqr - .065) < .005:
    #         found = 1
    #         print("Key is probably: ", possible_key, " f_sqr is ",sum_f_sqr)
    #     else:
    #         sum_sqr_frequencies[possible_key] = sum_f_sqr
    # if found:
    #     return found
    # else:
    #     # key.append(max(sum_sqr_frequencies, key=sum_sqr_frequencies.get))
    #     return ""

# o -> E
def swap1(text, x, y):
    text = text.replace(x, y.upper())
    print(text)
    return text

def change_letter(k, orig, replace):
    pos = abs(97 - ord(orig))
    letter = abs(97 - ord(replace))
    if k[pos] == -1:
        k[pos] = letter
    else:
        print(replace + " -> " + orig.upper() + " NOT POSSIBLE CAUSE " + chr(97 + k[pos]) + "(" + str(k[pos]) + ")")

    return k

def swap(k, orig, replace):
    for i in range(len(orig)):
        k = change_letter(k, list(orig)[i], list(replace)[i])

    return k

def view_key(key):
    a = [str(key[i]).ljust(2, ' ') for i in range(26)]
    b = [chr(65+i) + ' ' for i in range(26)]
    c = []
    for i in range(26):
        if key[i] == -1:
            c.append('  ')
        else:
            c.append(chr(97 + key[i]) + ' ')
    print(a)
    print(c)
    print(b)


key = [-1 for i in range(26)]
key = swap(key, 'i', 'b')
key = swap(key, 'v', 'i')
key = swap(key, 's', 'n')
key = swap(key, 'r', 'a')
key = swap(key, 'o', 'f')
key = swap(key, 'w', 'h')
key = swap(key, 'u', 'v')
key = swap(key, 'g', 't')
key = swap(key, 's', 'n')
key = swap(key, 'f', 'e')
key = swap(key, 'c', 'g')
key = swap(key, 'm', 's')
key = swap(key, 'k', 'q')
key = swap(key, 'b', 'k')
key = swap(key, 'p', 'c')
key = swap(key, 'y', 'y')
key = swap(key, 'the', 'luo')
key = swap(key, 'tha', 'luj')
key = swap(key, 'l', 'd')
key = swap(key, 'and', 'jmp')

txt = decode(text, key)


analyse(text)
view_key(key)

print(txt)
