prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = prijzen["aardbei"] * 0.8

reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €" + str(aanbieding)
reclame_tekst_2 = reclame_tekst [:62]
reclame_tekst_3 = reclame_tekst_2.upper() #Hoofdletters
reclame_tekst_4 = [reclame_tekst_3[:7], #VANDAAG List
                   reclame_tekst_3[8:10], #IN
                   reclame_tekst_3[11:13], #DE
                   reclame_tekst_3[14:24], #AANBIEDING
                   reclame_tekst_3[26:37], #VANILLE-IJS
                   reclame_tekst_3[39:46], #1 LITER
                   reclame_tekst_3[49:56], #SLECHTS
                   reclame_tekst_3[57:]] #€

for item in reclame_tekst_4:
    if len(item) > 4:
        print(item.upper())
    else:
        print(item.lower())


