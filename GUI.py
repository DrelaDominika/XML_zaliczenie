import tkinter as tk
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET
import Parser
from xml.dom import minidom

root = tk.Tk()
root.title("Ewidencja uczniów i ocen")  # title
filepath = r'C:\Users\Filip Szczepanski\source\repos\XML_zaliczenie2\oceny_uczniów.xml'  # var for XML file path
classA = False
classB = False
listaUczniow = []


canvas = tk.Canvas(height=400, width=400)
canvas.pack()


def add_path():  # chose path to XML file
    global filepath
    #filepath = tk.filedialog.askopenfilename(initialdir='/', title='wybierz plik z danymi uczniów')
    path_entry.insert(tk.END,filepath)


def open_file():
    global filepath
    os.startfile(filepath)


def write_XML():
    global filepath
    global lista
    file = r'C:\Users\Filip Szczepanski\source\repos\XML_zaliczenie2\szablon.xml'
    tree2 = ET.parse(file)
    rootParser = tree2.getroot()

    numer = int(students_entry.get()) #pobranie numeru z aplikacji
    imie = listaUczniow[numer][1]
    nazwisko = listaUczniow[numer][2]
    polski = listaUczniow[numer][3]
    angielski = listaUczniow[numer][4]
    matematyka = listaUczniow[numer][5]
    fizyka = listaUczniow[numer][6]
    geografia = listaUczniow[numer][7]
    srednia = listaUczniow[numer][8]

    uczenTag = ET.Element('uczen')  #treść XMLA

    imieTag = ET.SubElement(uczenTag,'imie')
    imieTag.text=str(imie)

    nazwiskoTag = ET.SubElement(uczenTag,'nazwisko')
    nazwiskoTag.text=str(nazwisko)

    polskiTag = ET.SubElement(uczenTag,'polski')
    polskiTag.text=str(polski)

    angielskiTag = ET.SubElement(uczenTag,'angielski')
    angielskiTag.text=str(angielski)

    matematykaTag = ET.SubElement(uczenTag,'matematyka')
    matematykaTag.text=str(matematyka)

    fizykaTag = ET.SubElement(uczenTag,'fizyka')
    fizykaTag.text=str(fizyka)

    geografiaTag = ET.SubElement(uczenTag,'geografia')
    geografiaTag.text=str(geografia)

    sredniaTag = ET.SubElement(uczenTag,'srednia')
    sredniaTag.text=str(srednia)


    raw = ET.tostring(uczenTag, encoding='unicode')

    pretty = minidom.parseString(raw).toprettyxml(indent='    ')

    with open(imie+ ' '+ nazwisko, 'w') as f:
        f.write(pretty)



    #ET.SubElement(tree2[0],'imieTEST')
    # ET.SubElement(,'nazwisko')
    # ET.SubElement(tree2[1],'polski')
    # ET.SubElement(tree2[1],'angielski')
    # ET.SubElement(tree2[1],'matematyka')
    # ET.SubElement(tree2[1],'fizyka')
    # ET.SubElement(tree2[1],'geografia')
    # ET.SubElement(tree2[1],'srednia')
    #ET.dump(tree2)





def parse_XML():
    global listaUczniow
    global filepath
    global lista
    tree = ET.parse(filepath)
    rootParser = tree.getroot()

    Parser.generating_lists(rootParser)

    listaUczniow = Parser.collecting_data()
    write_XML()
    #for e in listaUczniow:
    #    print(e)



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
