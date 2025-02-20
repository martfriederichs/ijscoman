from algemene_functies import mijn_functie_2 #les8hw12

def aanbieding_1(smaak, prijs, korting):
    aanbieding = prijs - (prijs*korting)
    return f"emmertje ijs (1 liter in de smaak {smaak}, van {prijs:2f} euro voor {aanbieding:2f} euro.)"

#les8hw6 & 7
def inkomsten_totaal(inkomsten = [220, 430, 125, 160, 205, 90, 345], btw = 0.09):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van de week is {totaal:2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."

#les8hw8
def laag_en_hoog(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]):
    hoogste_waarde = max(mijn_lijst)
    laagste_waarde = min(mijn_lijst)
    return [hoogste_waarde,laagste_waarde]

#les8hw9 & 10
def gemiddelde(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]):
    items = len(mijn_lijst)
    totaal = sum(mijn_lijst)
    bedrag = round(totaal/items)
    return f"De gemiddelde inkomsten deze week zijn {bedrag:.2f} euro."

#les8hw11
def meervoudig(invoer_lijst = [10,5,3,2,1,2,9]):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

#les8hw12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer