from part3_lesson1_problem import analyse
from polyalph_decode import decode
from EmailChallenge import fetch_email

text = fetch_email.get_mail_1()
# print(text)
i = 10
key = analyse(text, i)
print(i, key, len(key) == i)

raw = decode(text, key)
print(raw)
