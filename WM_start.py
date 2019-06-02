import datetime
import tkinter

# ****************************************************************************
# ****************************************************************************

# ermitteln des heutigen Tag
heute = datetime.date.today()
#heute = datetime.date(2017, 11, 10) #Testdatum

# ermitteln des nächsten Heiligen Abend in Bezug auf den Weihnachtsmarkt

aktuellesJahr = heute.year
if datetime.date(aktuellesJahr, 12, 28) > heute:
    DatumHeiligerAbend = datetime.date(aktuellesJahr, 12, 24)
else:
    DatumHeiligerAbend = datetime.date(aktuellesJahr+1, 12, 24)

# ermitteln der Adventssonntagen
wochentag=datetime.date.isoweekday(DatumHeiligerAbend)
if wochentag == 7:
    #der Heilige Abend ist, wenn ein Sonntag, auch gleichzeitg vierter Advent
    DatumVierterAdvend = DatumHeiligerAbend
else:
    DatumVierterAdvend = DatumHeiligerAbend - datetime.timedelta(days=wochentag)
    
DatumDritterAdvend = DatumVierterAdvend - datetime.timedelta(days=7)
DatumZweiterAdvend = DatumDritterAdvend - datetime.timedelta(days=7)
DatumErsterAdvend = DatumZweiterAdvend - datetime.timedelta(days=7)

# der Weihnachtsmarkt beginnt am Mittwoch vor dem ersten Advent,
# dass ist 4 Tage vorher
DatumBeginnWeihnachtsmarkt = DatumErsterAdvend - datetime.timedelta(days=4)

# Ermittlung des Status des Weihnachtsmarktes
information = ''
# überprüfen ob der Weihnachtsmarkt schon läuft
if DatumBeginnWeihnachtsmarkt < heute and heute < datetime.date(aktuellesJahr, 12, 28):
    information = 'läuft'
# oder überprüfen ob der Weihnachtsmarkt heute beginnt
elif DatumBeginnWeihnachtsmarkt == heute:
    information = 'beginnt heute'
# oder überprüfen wie lange es noch bis zum Weihnachtsmarkt ist
else:
    differenz = (DatumBeginnWeihnachtsmarkt-heute).days
    if differenz == 1:
        information = 'beginnt Morgen'
    else:
        information = 'beginnt in ' + str(differenz) + \
               ' Tagen, am ' + str(DatumBeginnWeihnachtsmarkt)

# Ausgabe der ermittelten Informationen
top = tkinter.Tk()
top.title('Weihnachtsmarkt')

# Textausgabe
ausgabe = tkinter.Label(top,\
                        text='Der Braunschweiger Weihnachtsmarkt\n'+information,\
                        fg='red', bg='#FFCFC9', font=('Arial', 16)).pack()

# Button zum Beenden des Programms
buttonNull = tkinter.Button(master=top, text='OK', bg='#FBD975', command=top.destroy).pack()
top.mainloop()