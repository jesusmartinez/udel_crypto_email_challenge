from collections import Counter
import functools

file = 'ch3'
with open(file, 'r') as f:
    txt = f.read()

print("Frequency")
freq = Counter(txt[idx] for idx in range(len(txt)))
freq_sorted = {k: val for k, val in sorted(freq.items(), key=lambda e : e[1], reverse=1)}
print(str(freq_sorted))

# frequency = {}
# for letter in singles:
#     frequency[letter] = float(singles[letter])/len(txt)
# frequency_sorted = {k: val for k, val in sorted(frequency.items(), key=lambda e : e[1], reverse=1)}
# print(str(dict(frequency_sorted)))


# print("-----------------------------------")
print("Bigram Frequency")
bigrams = Counter(txt[idx : idx + 2] for idx in range(len(txt) - 1))
bigrams_sorted = {k: val for k, val in sorted(bigrams.items(), key=lambda e : e[1], reverse=1)}
print(str(dict(bigrams_sorted)))
# bigram_frequency = {bi: float(count)/len(txt) for bi, count in bigrams.items()}
# bigram_frequency_sorted = {k: val for k, val in sorted(bigram_frequency.items(), key=lambda e : e[1], reverse=1)}
# print(str(dict(bigram_frequency_sorted)))


# print("-----------------------------------")
print("Trigram Frequency")
trigrams = Counter(txt[idx : idx + 3] for idx in range(len(txt) - 2))
trigrams_sorted = {k: val for k, val in sorted(trigrams.items(), key=lambda e : e[1], reverse=1)}
print(str(dict(trigrams_sorted)))
# trigram_frequency = {bi: float(count)/len(txt) for bi, count in trigrams.items()}
# trigram_frequency_sorted = {k: val for k, val in sorted(trigram_frequency.items(), key=lambda e : e[1], reverse=1)}
# print(str(dict(trigram_frequency_sorted)))


# Normal frequency
print("----------------------------------------------------------------------")
print("Normal Frequency")
normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
normal_freqs_sorted = {k: val for k, val in sorted(normal_freqs.items(), key=lambda e : e[1], reverse=1)}
# print(str(dict(normal_freqs_sorted)))
print(str(list(normal_freqs_sorted.keys())))
normal_bigram_freq = {'th': 0.03882543, 'he': 0.03681391, 'in': 0.02283899, 'er': 0.02178042, 'an': 0.02140460, 're': 0.01749394, 'nd': 0.01571977, 'on': 0.01418244, 'en': 0.01383239, 'at': 0.01335523, 'ou': 0.01285484, 'ed': 0.01275779, 'ha': 0.01274742, 'to': 0.01169655, 'or': 0.01151094, 'it': 0.01134891, 'is': 0.01109877, 'hi': 0.01092302, 'es': 0.01092301, 'ng': 0.01053385}
# print(str(dict(normal_bigram_freq)))
print(str(list(normal_bigram_freq.keys())))
normal_trigram_freq = {'the': 0.03508232,'and': 0.01593878,'ing': 0.01147042,'her': 0.00822444,'hat': 0.00650715,'his': 0.00596748,'tha': 0.00593593,'ere': 0.00560594,'for': 0.00555372,'ent': 0.00530771,'ion': 0.00506454,'ter': 0.00461099,'was': 0.00460487,'you': 0.00437213,'ith': 0.00431250,'ver': 0.00430732,'all': 0.00422758,'wit': 0.00397290,'thi': 0.00394796,'tio': 0.00378058}
# print(str(dict(normal_trigram_freq)))
print(str(list(normal_trigram_freq.keys())))


print("----------------------------------------------------------------------")
def compare_positions(pos1, pos2):
    bi_p1 = list(filter(lambda x : x > -1, pos1['bi_pos']))
    bi_p2 = list(filter(lambda y: y > -1, pos2['bi_pos']))
    tri_p1 = list(filter(lambda x : x > -1, pos1['tri_pos']))
    tri_p2 = list(filter(lambda y: y > -1, pos2['tri_pos']))

    return functools.reduce(lambda x, y : x and y, map(lambda p, q : p == q, bi_p1, bi_p2), True) and functools.reduce(lambda x, y : x and y, map(lambda p, q : p == q, tri_p1, tri_p2), True)
head = 5
# non_matched =
def get_positions(letter, bigrams, trigrams):
    bi_pos = [gram.rfind(letter) for gram in list(bigrams)[:head]]
    tri_pos = [gram.rfind(letter) for gram in list(trigrams)[:head]]
    return {
        'bi_pos': list(filter(lambda x : x > -1, bi_pos)),
        'tri_pos': list(filter(lambda x : x > -1, tri_pos))
    }

def match_letter():
    normal_positions = {}
    for normal_letter in list(normal_freqs_sorted.keys())[0:3]:
        normal_positions[normal_letter] = get_positions(normal_letter, normal_bigram_freq, normal_trigram_freq)

    print('Norm positions: ' + str(normal_positions))
    freq_positions = {}
    for freq_letter in list(freq_sorted.keys())[0:5]:
        freq_positions[freq_letter] = get_positions(freq_letter, bigrams_sorted, trigrams_sorted)

    print('Freq positions: ' + str(freq_positions))

    matches = {}
    for normal_letter, normal_pos in normal_positions.items():
        for freq_letter, freq_pos in freq_positions.items():
            if compare_positions(normal_pos, freq_pos):
                if matches.has_key(normal_letter) == 0:
                    matches[normal_letter] = []
                matches[normal_letter].append(freq_letter)
                print('Match normal_letter "' + normal_letter + '" ---> "' + freq_letter + '"')

    print('----> ' + str(matches) + ' matches')

match_letter()
