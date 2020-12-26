import tkinter as tk
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET
import Parser
# noinspection PyUnresolvedReferences
from xml.dom import minidom

root = tk.Tk()
root.title("Ewidencja uczniów i ocen")  # title
filepath = ''  # var for XML file path
classA = False
classB = False
listaUczniow = []
numer = 0

canvas = tk.Canvas(height=400, width=400)
canvas.pack()


def add_path():  # chose path to XML file
    global filepath
    filepath = tk.filedialog.askopenfilename(initialdir='/', title='wybierz plik z danymi uczniów')
    path_entry.insert(tk.END, filepath)


def open_file():
    global filepath
    os.startfile(filepath)


def write_XML():
    global filepath
    global lista
    global numer
    global classA
    global classB

    numer = int(students_entry.get())  # pobranie numeru z aplikacji
    imie = listaUczniow[numer][1]
    nazwisko = listaUczniow[numer][2]
    polski = listaUczniow[numer][3]
    angielski = listaUczniow[numer][4]
    matematyka = listaUczniow[numer][5]
    fizyka = listaUczniow[numer][6]
    geografia = listaUczniow[numer][7]
    srednia = listaUczniow[numer][8]

    uczenTag = ET.Element('uczen')  # treść XMLA

    imieTag = ET.SubElement(uczenTag, 'imie')
    imieTag.text = str(imie)

    nazwiskoTag = ET.SubElement(uczenTag, 'nazwisko')
    nazwiskoTag.text = str(nazwisko)

    polskiTag = ET.SubElement(uczenTag, 'polski')
    polskiTag.text = str(polski)

    angielskiTag = ET.SubElement(uczenTag, 'angielski')
    angielskiTag.text = str(angielski)

    matematykaTag = ET.SubElement(uczenTag, 'matematyka')
    matematykaTag.text = str(matematyka)

    fizykaTag = ET.SubElement(uczenTag, 'fizyka')
    fizykaTag.text = str(fizyka)

    geografiaTag = ET.SubElement(uczenTag, 'geografia')
    geografiaTag.text = str(geografia)

    sredniaTag = ET.SubElement(uczenTag, 'srednia')
    sredniaTag.text = str(srednia)

    if ((numer in range(1, 10) and classA) or (numer in range(11, 20) and classB)):
        raw = ET.tostring(uczenTag, encoding='unicode')  # zapisywanie xmla do pliku
        pretty = minidom.parseString(raw).toprettyxml(indent='    ')
        with open(imie + ' ' + nazwisko, 'w') as f:
            f.write(pretty)
    else:
        error_label.configure(text='BRAK UCZNIA O PODANYM NUMERZE W DANEJ KLASIE', fg='red')


def display_info():
    global filepath
    global lista
    global numer
    global listaUczniow
    global classA
    global classB

    tree = ET.parse(filepath)
    rootParser = tree.getroot()

    Parser.generating_lists(rootParser)

    listaUczniow = Parser.collecting_data()

    numer = int(students_entry.get())  # pobranie numeru z aplikacji
    imie = listaUczniow[numer][1]
    nazwisko = listaUczniow[numer][2]
    polski = listaUczniow[numer][3]
    angielski = listaUczniow[numer][4]
    matematyka = listaUczniow[numer][5]
    fizyka = listaUczniow[numer][6]
    geografia = listaUczniow[numer][7]
    srednia = listaUczniow[numer][8]

    if ((numer in range(1, 10) and classA) or (numer in range(11, 20) and classB)):
        info_label.config(text=f"Średnie ucznia o imieniu: {str(imie)} {str(nazwisko)} \n"  # displaying info in label
                               f"j. polski:      {str(polski)} \n"
                               f"j. angielski:   {str(angielski)} \n"
                               f"matematyka:     {str(matematyka)} \n"
                               f"fizyka:         {str(fizyka)} \n"
                               f"geografia:      {str(geografia)} \n"
                               f"srednia ogólna: {str(srednia)}"
                          )
    else:
        error_label.configure(text='BRAK UCZNIA O PODANYM NUMERZE W DANEJ KLASIE', fg='red')


def checkboxA():
    global classA
    global classB
    classA = True
    classB = False
    students_checkbox2.deselect()


def checkboxB():
    global classB
    global classA
    classB = True
    classA = False
    students_checkbox1.deselect()


frame_path = tk.Frame(root, borderwidth=2, relief='ridge')  # frame for path section
frame_path.place(relwidth=0.9, relheight=0.15, relx=0.05, rely=0.05)

path_button = tk.Button(frame_path, text='Wybierz ścieżkę', justify='center', command=add_path)
path_button.place(rely=0.03, relheight=0.45, relwidth=0.28)

path_entry = tk.Entry(frame_path, )
path_entry.place(rely=0.03, relheight=0.45, relwidth=0.7, relx=0.29)

open_button = tk.Button(frame_path, text='Otwórz plik', justify='center',
                        command=open_file)  # button for opening xsl file
open_button.place(rely=0.5, relheight=0.45, relwidth=0.28)

frame_students = tk.Frame(root, borderwidth=2, relief='ridge')  # frame for selecting students
frame_students.place(relwidth=0.9, relheight=0.15, relx=0.05, rely=0.24)

students_checkbox1 = tk.Checkbutton(frame_students, text='Klasa A', command=checkboxA)
students_checkbox1.grid(row=1, column=1)

students_checkbox2 = tk.Checkbutton(frame_students, text='Klasa B', command=checkboxB)
students_checkbox2.grid(row=2, column=1)

students_label = tk.Label(frame_students, text='Podaj nr ucznia', padx=40)
students_label.grid(row=1, column=2)

students_entry = tk.Entry(frame_students)
students_entry.grid(row=2, column=2)

students_button = tk.Button(frame_students, text='Wyświetl dane', command=display_info)
students_button.place(relx=0.7, rely=0.03, relheight=0.45, relwidth=0.28)

students_button2 = tk.Button(frame_students, text='Eksportuj dane', command=write_XML)
students_button2.place(relx=0.7, rely=0.5, relheight=0.45, relwidth=0.28)

info_label = tk.Label(root, bg='white', text='', borderwidth=2,
                      relief='ridge')  # label for displaying chosen student`s info
info_label.place(relwidth=0.9, relheight=0.5, relx=0.05, rely=0.45)

error_label = tk.Label(root, text='', justify='center')
error_label.place(relwidth=0.9, relheight=0.06, relx=0.05, rely=0.39)
root.mainloop()  # keep as the last line
