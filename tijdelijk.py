from helper import decodeer

def print_aanbieding():
    prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
    }

    aanbieding = prijzen["aardbei"] * 0.8

    reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €" + str(aanbieding)
    reclame_tekst_2 = reclame_tekst [:62]
    reclame_tekst_3 = reclame_tekst_2.upper() #Hoofdletters
    reclame_tekst_4 = reclame_tekst_3.split() 

    for item in reclame_tekst_4:
        if len(item) > 4:
            print(item.upper())
        else:
            print(item.lower())


decodeer("Aanbieding")
print_aanbieding()