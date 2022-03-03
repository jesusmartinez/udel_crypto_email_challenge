from topWords import top_words,top_100_words

def andy_fitness(text):
    text = text.lower()
    score = 0
    for common in top_words:
        score += text.count(common) * len(text)
    return score

def fitness(text):
    text = text.lower()
    score = 0
    for common in top_100_words:
        score += text.count(common) * len(common)

    return score / len(text)

def matches(text):
    score = 0
    score
    words = []
    txt_length = len(text)
    for common in top_words:
        match = text.count(common)
        if match > 0:
            score += match
            words.append(common)
    # print(words, score)
    # return score / len(text)

    for w in words:
        text = text.replace(w, '')
    score = 1 - (len(text) / txt_length)
    # print(score, text)
    return score



# f = fitness("TRULYTOENJOYBODILYWARMTHSOMESMALLPARTOFYOUMUSTBECOLDFORTHEREISNOQUALITYINTHISWORLDTHATISNOTWHATITISMERELYBYCONTRASTNOTHINGEXISTSINITSELFWESHOULDREGRETOURMISTAKESANDLEARNFROMTHEMBUTNEVERCARRYTHEMFORWARDINTOTHEFUTUREWITHUSOHFRIENDJOHNITISASTRANGEWORLDASADWORLDAWORLDFULLOFMISERIESANDWOESANDTROUBLESANDYETWHENKINGLAUGHCOMEHEMAKETHEMALLDANCETOTHETUNEHEPLAYITSEEMSTOMENOWIFIWASTOFINDFATHERATHOMETONIGHTISHOULDBEHAVEDIFFERENTBUTTHERESNOKNOWINGPERHAPSNOTHINGUDBEALESSONTOUSIFITDIDNTCOMETOOLATEALLTHINGSAREREADYIFOURMINDSBESOSHEINDULGEDINMELANCHOLYTHATCHEAPESTANDMOSTACCESSIBLEOFLUXURIESDESPAIRHASITSOWNCALMS".lower())
# m = matches("TRULYTOENJOYBODILYWARMTHSOMESMALLPARTOFYOUMUSTBECOLDFORTHEREISNOQUALITYINTHISWORLDTHATISNOTWHATITISMERELYBYCONTRASTNOTHINGEXISTSINITSELFWESHOULDREGRETOURMISTAKESANDLEARNFROMTHEMBUTNEVERCARRYTHEMFORWARDINTOTHEFUTUREWITHUSOHFRIENDJOHNITISASTRANGEWORLDASADWORLDAWORLDFULLOFMISERIESANDWOESANDTROUBLESANDYETWHENKINGLAUGHCOMEHEMAKETHEMALLDANCETOTHETUNEHEPLAYITSEEMSTOMENOWIFIWASTOFINDFATHERATHOMETONIGHTISHOULDBEHAVEDIFFERENTBUTTHERESNOKNOWINGPERHAPSNOTHINGUDBEALESSONTOUSIFITDIDNTCOMETOOLATEALLTHINGSAREREADYIFOURMINDSBESOSHEINDULGEDINMELANCHOLYTHATCHEAPESTANDMOSTACCESSIBLEOFLUXURIESDESPAIRHASITSOWNCALMS".lower())
# print(f, m, (f+m) / 2)
#
# print()
# f = fitness("andyisthebest")
# m = matches("andyisthebest")
# print(f, m, (f+m) / 2)
#
# print()
# f = fitness("bgfmeonnlujlbujiokoomjnkdbmpjnjsfdokvlblbnkolloalfdojamhbnpfsdjlolujmmoioalfdojambljljddmoioaefatolhujlyfvjaoefanvaodyluohfadphbddmflsjqoblyfvanlaomtluluomblgjmmoioakoyfvahojqmonnjasfayfvanodebmbljmpblhbddmoioakovnoplfuvalyfvmffmobnoioalfffdplfpfjeffdbnulubmtpfyfvqmfhjmylubmtfmojaluhubguujnmfljpjmtoafvnnbpobeblbnsbnujmpdopjmpoxjttoajlopmfcdjgohfaluqmfhbmtybodpnblnodejlnbtuljmplufnoluodojnlbmiblbmtfmebanlibohsjydojioluosfnlujvmlbmtcbglvaonvcfmluohjddnfesosfaysfambmtsjpojgfmnbpoajkdopbeeoaomgobmsytomoajdcafncoglfedbeojmpkabtulomopblnfsvgulujlblngjagodynoosopluonjsobtmfajmgobnluocjaomlfeeojax")
# m = matches("bgfmeonnlujlbujiokoomjnkdbmpjnjsfdokvlblbnkolloalfdojamhbnpfsdjlolujmmoioalfdojambljljddmoioaefatolhujlyfvjaoefanvaodyluohfadphbddmflsjqoblyfvanlaomtluluomblgjmmoioakoyfvahojqmonnjasfayfvanodebmbljmpblhbddmoioakovnoplfuvalyfvmffmobnoioalfffdplfpfjeffdbnulubmtpfyfvqmfhjmylubmtfmojaluhubguujnmfljpjmtoafvnnbpobeblbnsbnujmpdopjmpoxjttoajlopmfcdjgohfaluqmfhbmtybodpnblnodejlnbtuljmplufnoluodojnlbmiblbmtfmebanlibohsjydojioluosfnlujvmlbmtcbglvaonvcfmluohjddnfesosfaysfambmtsjpojgfmnbpoajkdopbeeoaomgobmsytomoajdcafncoglfedbeojmpkabtulomopblnfsvgulujlblngjagodynoosopluonjsobtmfajmgobnluocjaomlfeeojax")
# print(f, m, (f+m) / 2)