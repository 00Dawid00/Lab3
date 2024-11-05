ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
numery = [1, 2, 3, 4, 5]
mieszkania = ["/1", "/2", "/3", "/4", "/5", "/6", "/7", "/8", "/9", "/10"]

for ulica in ulice:
    for numer in numery:
        for mieszkanie in mieszkania:
            print(f"{ulica} {numer}{mieszkanie}")
