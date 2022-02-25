# Andy frequency function

def getfreq(loweronly):
    frequency = {}
    for ascii in range(ord('a'), ord('a') + 26):
        frequency[chr(ascii)] = float(loweronly.count(chr(ascii))) / len(loweronly)

    sum_freq_squared = 0.0
    for ltr in frequency:
        sum_freq_squared += frequency[ltr] * frequency[ltr]

    return sum_freq_squared