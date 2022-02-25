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



s = fitness("TRULYTOENJOYBODILYWARMTHSOMESMALLPARTOFYOUMUSTBECOLDFORTHEREISNOQUALITYINTHISWORLDTHATISNOTWHATITISMERELYBYCONTRASTNOTHINGEXISTSINITSELFWESHOULDREGRETOURMISTAKESANDLEARNFROMTHEMBUTNEVERCARRYTHEMFORWARDINTOTHEFUTUREWITHUSOHFRIENDJOHNITISASTRANGEWORLDASADWORLDAWORLDFULLOFMISERIESANDWOESANDTROUBLESANDYETWHENKINGLAUGHCOMEHEMAKETHEMALLDANCETOTHETUNEHEPLAYITSEEMSTOMENOWIFIWASTOFINDFATHERATHOMETONIGHTISHOULDBEHAVEDIFFERENTBUTTHERESNOKNOWINGPERHAPSNOTHINGUDBEALESSONTOUSIFITDIDNTCOMETOOLATEALLTHINGSAREREADYIFOURMINDSBESOSHEINDULGEDINMELANCHOLYTHATCHEAPESTANDMOSTACCESSIBLEOFLUXURIESDESPAIRHASITSOWNCALMS")
#s = fitness("bgfmeonnlujlbujiokoomjnkdbmpjnjsfdokvlblbnkolloalfdojamhbnpfsdjlolujmmoioalfdojambljljddmoioaefatolhujlyfvjaoefanvaodyluohfadphbddmflsjqoblyfvanlaomtluluomblgjmmoioakoyfvahojqmonnjasfayfvanodebmbljmpblhbddmoioakovnoplfuvalyfvmffmobnoioalfffdplfpfjeffdbnulubmtpfyfvqmfhjmylubmtfmojaluhubguujnmfljpjmtoafvnnbpobeblbnsbnujmpdopjmpoxjttoajlopmfcdjgohfaluqmfhbmtybodpnblnodejlnbtuljmplufnoluodojnlbmiblbmtfmebanlibohsjydojioluosfnlujvmlbmtcbglvaonvcfmluohjddnfesosfaysfambmtsjpojgfmnbpoajkdopbeeoaomgobmsytomoajdcafncoglfedbeojmpkabtulomopblnfsvgulujlblngjagodynoosopluonjsobtmfajmgobnluocjaomlfeeojax")
print("Score: " + str(s))