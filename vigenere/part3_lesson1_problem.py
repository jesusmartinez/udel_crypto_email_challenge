import polyalph_decode

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

def analyse(text, keyLength):
    subtexts = [text[i::keyLength] for i in range(keyLength)]
    frequencies = []
    key = []

    for i in range(keyLength):
        frequency = {}
        for ascii in range(ord('a'), ord('a')+26):
            enc1 = subtexts[i].count(chr(ascii))
            frequency[chr(ascii)] = float(enc1)/len(subtexts[i])
        frequencies.append(frequency)

        # print(i, frequency)
        found = -1
        sum_sqr_frequencies = {}
        for possible_key in range(1, 26):
            sum_f_sqr = 0.0
            for ltr in normal_freqs:
                caesar_guess = shiftBy(ltr, possible_key)
                sum_f_sqr += normal_freqs[ltr]*frequency[caesar_guess] # IMPORTANT
            if abs(sum_f_sqr - .065) < .005:
                # key.append(possible_key)
                found = possible_key
                # print("For subtext " + str(i) + " key is probably: ", possible_key, " f_sqr is ", sum_f_sqr)
            else:
                sum_sqr_frequencies[possible_key] = sum_f_sqr
        # Add the guess if it was found
        if found > -1:
            key.append(found)
        # If not, pick the highest guess
        else:
            key.append(max(sum_sqr_frequencies, key=sum_sqr_frequencies.get))

    return key
