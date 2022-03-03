import random

def encode(plain):
    cols = random.randint(8,10)
    key = list(range(cols))
    random.shuffle(key)
    return "".join(plain[i::cols].lower() for i in key), key

def decode(code, key):
    decode = {}
    txt_length = len(code)
    key_length = len(key)
    extras = txt_length % key_length
    total_rows = -(txt_length // -key_length)
    counter = 0
    for x in key:
        if x < extras:
            rows = total_rows
        else:
            rows = total_rows - 1
        for y in range(rows):
            pos = x + (key_length * y)
            if counter < txt_length:
                decode[pos] = code[counter]
                counter += 1

    return "".join([val for k, val in sorted(decode.items(), key=lambda e: e[0])])

# print(ciphers.col_trans("ANDYISTHEBEST"))
# print(col_trans_dec('dthbaetseynsi', [2, 7, 9, 0, 6, 5, 8, 3, 1, 4]))
# print(col_trans_dec('dthbaetseynsi', [7,2, 0, 9, 6, 5, 8, 3, 1, 4]))

# print(ciphers.col_trans("ILikePizza"))
#print(col_trans_dec('izzkilpeia', [6, 8, 7, 3, 2, 1, 5, 4, 0]))
# print(decode('oidtsnsutoctieirnoesuvhtp', [6, 0, 3, 5, 2, 7, 4, 1]))

def check(txt):
    code, key = encode(txt)
    # print(code, key)
    result = decode(code, key)
    # print(result)
    if txt.lower() == result:
        print("OK")
    else:
        print("ERR!")
        print(txt, code, key, len(key))
        print(result)

# check("ANDYISTHEBEST")
# check("TheUSConstitutionprovides")
# check("TheUSConstitutionprovidesforafederaldistrictundertheexclusivejurisdictionofCongressthedistrictisthereforenotapartofanyUSstatenorisitoneitselfThesigningoftheResidenceActonJulyapprovedthecreationofacapitaldistrictlocatedalongthePotomacRivernearthecountrysEastCoastTheCityofWashingtonwasfoundedintoserveasthenationalcapitalandCongresshelditsfirstsessionthereinIntheterritoryformerlypartofMarylandandVirginiaincludingthesettlementsofGeorgetownandAlexandriaofficiallybecamerecognizedasthefederaldistrictInCongressreturnedthelandoriginallycededbyVirginiaincludingthecityofAlexandriainitcreatedasinglemunicipalgovernmentfortheremainingportionofthedistrictTherehavebeeneffortstomakethecityintoastatesincethesamovementthathasgainedmomentuminrecentyearsandastatehoodbillpassedtheHouseofRepresentativesin")