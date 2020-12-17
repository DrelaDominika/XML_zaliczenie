import tkinter as tk
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET


root = tk.Tk()
root.title("Ewidencja uczniów i ocen")  # title
filepath = r'C:\Users\Filip Szczepanski\source\repos\XML_zaliczenie2\oceny_uczniów.xml'  # var for XML file path
classA = False
classB = False
lista = []

canvas = tk.Canvas(height=400, width=400)
canvas.pack()


def add_path():  # chose path to XML file
    global filepath
    filepath = tk.filedialog.askopenfilename(initialdir='/', title='wybierz plik z danymi uczniów')
    path_entry.insert(tk.END,filepath)


def open_file():
    global filepath
    os.startfile(filepath)

def parse_XML():
    global filepath
    global lista
    tree = ET.parse(filepath)
    rootParser = tree.getroot()

    #tablica dwuwymiarowa dla każdego ucznia imie,naziwsko,polski.avg,matematyka.avg.....
    #find uczen where id_ucznia = x (wczytanie z gui od 1 do 20
    #write uczen.imie, uczen.nazwisko
    #write uczen/przedmioty/polski/oceny .split(,) .avg()
    #write uczen/przedmioty/polski/angielski ....

    for uczen in rootParser.iter('imie'):
        print(uczen.text)
        lista.append()

    for uczen in rootParser.iter('nazwisko'):
        print(uczen.text)

    # for uczen in rootParser.iter('przedmioty'):
    #     for el in rootParser.iter('oceny'):
    #         print(przedmioty.text)

def checkboxA():
    global classA
    classA = not classA
    students_checkbox2.deselect()

def checkboxB():
    global classB
    classB = not classB
    students_checkbox1.deselect()

frame_path = tk.Frame(root)  # frame for path section
frame_path.place(relwidth=0.9, relheight=0.08, relx=0.05, rely=0.05)

path_button = tk.Button(frame_path, text='Wybierz ścieżkę', justify='center',command=add_path)
path_button.place(relheight=1, relwidth=0.3)

path_entry = tk.Entry(frame_path, )
path_entry.place(relheight=1, relwidth=0.7, relx=0.3)

open_button =tk.Button(root,text='Otwórz plik',command=open_file) # open button
open_button.place(relx=0.4,rely=0.2)

frame_parse = tk.Frame(root)  # frame for parsing
frame_parse.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.3)

parse_button = tk.Button(frame_parse, text='XML działaj', justify='center',command=parse_XML)
parse_button.place(relheight=1, relwidth=0.4)


frame_students = tk.Frame(root, borderwidth=2, relief='ridge')  # frame for selecting students
frame_students.place(relwidth=0.9, relheight=0.15, relx=0.05, rely=0.5)

students_checkbox1 = tk.Checkbutton(frame_students, text='Klasa A', command=checkboxA)
students_checkbox1.grid(row=1, column=1)

students_checkbox2 = tk.Checkbutton(frame_students, text='Klasa B', command=checkboxB)
students_checkbox2.grid(row=2, column=1)

students_label = tk.Label(frame_students, text='Podaj nr ucznia', padx=40)
students_label.grid(row=1, column=2)

students_entry = tk.Entry(frame_students)
students_entry.grid(row=2,column=2)

students_button = tk.Button(frame_students,text= 'Wyświetl dane')
students_button.place(relx=0.7,rely=0.1,relheight=0.8,relwidth=0.28)




root.mainloop()# keep as the last line
