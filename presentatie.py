def presenteer(mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}, Totaal = 50):
    Uitvoer = []
    for k,v in mijn_dict.items():
        Uitvoer.append(f"{k} : {v} euro")
    Uitvoer.append(26*"=")
    Uitvoer.append(f"Totaal : {Totaal} euro")
    
    for item in Uitvoer:
        print(item)

