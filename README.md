#Substitution
- Has 26! posible keys, whereas Caesar is only 26
abcdefghijklmnopqrstuvwxz - 26 -letters

$ cat ch1 | sed 's;.;&=;g' | tr '=' '\012' | sort | uniq -c | sort -rn

ch1 26 <--
ch2 23 <---
ch3 26 <--
ch4 25 <--
ch5 23

Bigram & Trigram Analysis
ch3 26 <--
ch4 25 <--

-----
ch1
Norm positions: {'e': {'bi_pos': [1, 0], 'tri_pos': [2, 1]}, 't': {'bi_pos': [0], 'tri_pos': [0, 2]}, 'a': {'bi_pos': [0], 'tri_pos': [0, 1]}}
Freq positions: {'i': {'bi_pos': [0], 'tri_pos': [1, 0]}, 'h': {'bi_pos': [0], 'tri_pos': [0]}, 'c': {'bi_pos': [0], 'tri_pos': [2, 1]}, 'u': {'bi_pos': [1], 'tri_pos': [2, 0]}, 't': {'bi_pos': [], 'tri_pos': []}}
Match normal_letter "e" ---> "t"
Match normal_letter "t" ---> "h"
Match normal_letter "t" ---> "t"
Match normal_letter "a" ---> "h"
Match normal_letter "a" ---> "t"
----> 5 matches

ch2
Norm positions: {'e': {'bi_pos': [1, 0], 'tri_pos': [2, 1]}, 't': {'bi_pos': [0], 'tri_pos': [0, 2]}, 'a': {'bi_pos': [0], 'tri_pos': [0, 1]}}
Freq positions: {'o': {'bi_pos': [0], 'tri_pos': [2, 2, 1]}, 'l': {'bi_pos': [0, 1], 'tri_pos': [0]}, 'm': {'bi_pos': [1, 1], 'tri_pos': [1]}, 'f': {'bi_pos': [], 'tri_pos': [1]}, 'j': {'bi_pos': [0], 'tri_pos': []}}
Match normal_letter "t" ---> "l"
Match normal_letter "t" ---> "j"
Match normal_letter "a" ---> "l"
Match normal_letter "a" ---> "j"
----> 4 matches

ch3
Norm positions: {'e': {'bi_pos': [1, 0], 'tri_pos': [2, 1]}, 't': {'bi_pos': [0], 'tri_pos': [0, 2]}, 'a': {'bi_pos': [0], 'tri_pos': [0, 1]}}
Freq positions: {'g': {'bi_pos': [0, 0], 'tri_pos': []}, 'k': {'bi_pos': [1], 'tri_pos': [2]}, 'p': {'bi_pos': [0], 'tri_pos': []}, 'w': {'bi_pos': [], 'tri_pos': [2, 0]}, 'n': {'bi_pos': [], 'tri_pos': [2, 1, 2]}}
Match normal_letter "e" ---> "k"
Match normal_letter "e" ---> "n"
Match normal_letter "t" ---> "g"
Match normal_letter "t" ---> "p"
Match normal_letter "a" ---> "g"
Match normal_letter "a" ---> "p"
----> 6 matches

ch4
Norm positions: {'e': {'bi_pos': [1, 0], 'tri_pos': [2, 1]}, 't': {'bi_pos': [0], 'tri_pos': [0, 2]}, 'a': {'bi_pos': [0], 'tri_pos': [0, 1]}}
Freq positions: {'d': {'bi_pos': [0, 1], 'tri_pos': [0, 0]}, 'i': {'bi_pos': [], 'tri_pos': [2]}, 'p': {'bi_pos': [1, 1], 'tri_pos': [1, 2]}, 'm': {'bi_pos': [1], 'tri_pos': [2]}, 'e': {'bi_pos': [], 'tri_pos': []}}
Match normal_letter "e" ---> "i"
Match normal_letter "e" ---> "m"
Match normal_letter "e" ---> "e"
Match normal_letter "t" ---> "e"
Match normal_letter "a" ---> "e"
----> 5 matches

ch5
Norm positions: {'e': {'bi_pos': [1, 0], 'tri_pos': [2, 1]}, 't': {'bi_pos': [0], 'tri_pos': [0, 2]}, 'a': {'bi_pos': [0], 'tri_pos': [0, 1]}}
Freq positions: {'e': {'bi_pos': [0, 1, 1, 1], 'tri_pos': [1, 0]}, 't': {'bi_pos': [0, 0], 'tri_pos': [0, 2]}, 'o': {'bi_pos': [1, 1], 'tri_pos': [1, 2, 1, 0]}, 'n': {'bi_pos': [], 'tri_pos': [2, 0]}, 'a': {'bi_pos': [0], 'tri_pos': []}}
Match normal_letter "t" ---> "t"
Match normal_letter "t" ---> "a"
Match normal_letter "a" ---> "a"
----> 3 matches

#Tips
- Write a decryption function that takes a simple correct key and works
- Frequency Analysis
- Know effort of Brute Force

