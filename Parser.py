import tkinter as tk
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET

listaUczniow = []
listaImion = []
listaNazwisk = []
listaPolski = []
listaAngielski = []
listaMatematyka = []
listaFizyka = []
listaGeografia = []
sredniaKlasaA = 0
sredniaKlasaB = 0


def info_collector(index, imie, nazwisko, polski, angielski, matematyka, fizyka, geografia,srednia):
    daneUcznia = [index, imie, nazwisko, polski, angielski, matematyka, fizyka,geografia,srednia]
    return daneUcznia

def generating_lists(rootParser):

    for uczen in rootParser.iter('imie'):
        listaImion.append(uczen.text)

    for uczen in rootParser.iter('nazwisko'):
        listaNazwisk.append(uczen.text)

    for e in rootParser.findall("./uczniowie/uczen/przedmioty/polski/oceny"):
        listaPolski.append(e.text)

    for e in rootParser.findall("./uczniowie/uczen/przedmioty/angielski/oceny"):
        listaAngielski.append(e.text)

    for e in rootParser.findall("./uczniowie/uczen/przedmioty/matematyka/oceny"):
        listaMatematyka.append(e.text)

    for e in rootParser.findall("./uczniowie/uczen/przedmioty/fizyka/oceny"):
        listaFizyka.append(e.text)

    for e in rootParser.findall("./uczniowie/uczen/przedmioty/geografia/oceny"):
        listaGeografia.append(e.text)


def collecting_data():
    global listaUczniow
    global listaImion
    global listaNazwisk
    global listaPolski
    global listaAngielski
    global listaMatematyka
    global listaFizyka
    global listaGeografia

    index = 0
    listaUczniow=[]

    for e in range(20):
        imie = listaImion[e]
        nazwisko = listaNazwisk[e]
        #polski
        pInt = [float(x) for x in listaPolski[e].split(",")]
        pSize = len(pInt)
        polski=(sum(pInt)/pSize)
        polski = round(polski,2)

        #angielski
        aInt = [float(x) for x in listaAngielski[e].split(",")]
        aSize = len(aInt)
        angielski=(sum(aInt)/aSize)
        angielski = round(angielski,2)

        #matematyka
        mInt = [float(x) for x in listaMatematyka[e].split(",")]
        mSize = len(mInt)
        matematyka=(sum(mInt)/mSize)
        matematyka = round(matematyka,2)

        #fizyka
        fInt = [float(x) for x in listaFizyka[e].split(",")]
        fSize = len(fInt)
        fizyka=(sum(fInt)/fSize)
        fizyka =round(fizyka,2)

        #geografia
        gInt = [float(x) for x in listaGeografia[e].split(",")]
        gSize = len(gInt)
        geografia=(sum(gInt)/gSize)
        geografia = round(geografia,2)

        #średnia
        srednia = ((polski+angielski+matematyka+fizyka+geografia)/5)
        srednia = round(srednia,2)

        index=index+1
        listaUczniow.append(info_collector(index, imie, nazwisko, polski, angielski, matematyka, fizyka, geografia,srednia))
    return listaUczniow
