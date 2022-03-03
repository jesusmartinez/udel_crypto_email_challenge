# Andy frequency function
import fetch_email

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
def getfreq(loweronly):
    frequency = {}
    for ascii in range(ord('a'), ord('a') + 26):
        frequency[chr(ascii)] = float(loweronly.count(chr(ascii))) / len(loweronly)
    # print(frequency)
    sum_freq_squared = 0.0

    for ltr in frequency:
        sum_freq_squared += frequency[ltr] * frequency[ltr]

    return sum_freq_squared

# print(getfreq("andyisthebest"))
# print(getfreq("TRULYTOENJOYBODILYWARMTHSOMESMALLPARTOFYOUMUSTBECOLD".lower()))
# Caesar: 0.07100591715976333

# 0.06503085446601505
# print(getfreq(fetch_email.get_mail_5()))

# 0.05120264852934553
# print(getfreq(fetch_email.get_mail_4()))

# 0.04694578360421024
# print(getfreq(fetch_email.get_mail_3()))

# 0.06745191658033421
# print(getfreq(fetch_email.get_mail_2()))
