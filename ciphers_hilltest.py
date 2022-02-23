import ciphers


[ct, keym] = ciphers.hill_enc("MARTINEZ")
print(ct, keym)

pt = ciphers.hill_dec('martinez', keym)
print(pt)