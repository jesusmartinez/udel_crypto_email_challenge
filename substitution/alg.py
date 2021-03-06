import random


def substitution(plaintext):
    letters = list(range(26))
    random.shuffle(letters)
    cipher = plaintext
    for i in range(26):
        pt = chr(65+i)
        cipher = cipher.replace(pt, chr(97+letters[i]))
    return cipher, letters


def decode(cipher, key):
    plain = cipher
    n = 0
    for i in key:
        if i > -1:
            pt = chr(97 + i)
            plain = plain.replace(pt, chr(65 + n))
        n += 1
    return plain


def check(txt):
    code, key = substitution(txt)
    print(code, key)
    result = decode(code, key)
    print(result)
    if txt == result:
        print("OK")
    else:
        print("ERR!")
        print(txt, code, key, len(key))
        print(result)

# check("HELLOWORLD")
# check("ANDYISTHEBEST")
# check("THEUSCONSTITUTIONPROVIDES")
# check("THEUSCONSTITUTIONPROVIDESFORAFEDERALDISTRICTUNDERTHEEXCLUSIVEJURISDICTIONOFCONGRESSTHEDISTRICTISTHEREFORENOTAPARTOFANYUSSTATENORISITONEITSELFTHESIGNINGOFTHERESIDENCEACTONJULYAPPROVEDTHECREATIONOFACAPITALDISTRICTLOCATEDALONGTHEPOTOMACRIVERNEARTHECOUNTRYSEASTCOASTTHECITYOFWASHINGTONWASFOUNDEDINTOSERVEASTHENATIONALCAPITALANDCONGRESSHELDITSFIRSTSESSIONTHEREININTHETERRITORYFORMERLYPARTOFMARYLANDANDVIRGINIAINCLUDINGTHESETTLEMENTSOFGEORGETOWNANDALEXANDRIAOFFICIALLYBECAMERECOGNIZEDASTHEFEDERALDISTRICTINCONGRESSRETURNEDTHELANDORIGINALLYCEDEDBYVIRGINIAINCLUDINGTHECITYOFALEXANDRIAINITCREATEDASINGLEMUNICIPALGOVERNMENTFORTHEREMAININGPORTIONOFTHEDISTRICTTHEREHAVEBEENEFFORTSTOMAKETHECITYINTOASTATESINCETHESAMOVEMENTTHATHASGAINEDMOMENTUMINRECENTYEARSANDASTATEHOODBILLPASSEDTHEHOUSEOFREPRESENTATIVESIN")