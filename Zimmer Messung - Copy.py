#Zimmermessung
#Wohnungmessung
#
#
a=0
x =1
Wohnung= 0

print('Möchten Sie einzelne Zimmer oder eine Wohung messen?(Für Wohnung geben Sie 1 ein, für Zimmer bitte 2 eingeben)')
choice=int(input())
while a ==0 :#damit viele Zimmer messen kann
    Gesamt_Rechteck=0
    print('Bitte geben sie den Namen des Zimmers ein:')
    zimmer=str(input())
    print ('Aus wie vielen Rechtecken besteht der Raum?')#Wenn ein 
    b=int(input())
    for x in  range(0, b):
        print("Bitte geben Sie die Länge des Rechtecks in Metern an:(Teilraum / Raum",x+1,  ")")
        länge=int(input())
        print("Bitte geben Sie die Breite des Rechtecks in Metern an:(Teilraum / Raum",x+1,  ")")
        breite =int(input())
        Rechteck = länge*breite
        Gesamt_Rechteck= Gesamt_Rechteck + Rechteck

    print('Das Zimmer "', zimmer,'" ist ', Gesamt_Rechteck, 'm² groß.')
    if choice == 1 :
        Wohnung = Wohnung + Gesamt_Rechteck
        
    print('Möchten Sie mehr Zimmer messen?(Wenn ja, geben Sie 0)')#wenn wir fertig sind oder weiter machen möchten
    a=int(input())

if choice == 1 :
    print('Die Wohnung ist ', Wohnung,'m² groß.')




