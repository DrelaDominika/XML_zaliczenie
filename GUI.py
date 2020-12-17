import tkinter as tk
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET


root = tk.Tk()
root.title("Ewidencja uczniów i ocen")  # title
filepath = ''  # var for XML file path

canvas = tk.Canvas(height=300, width=400)
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


frame_path = tk.Frame(root)  # frame for path section
frame_path.place(relwidth=0.9, relheight=0.08, relx=0.05, rely=0.05)

path_button = tk.Button(frame_path, text='Wybierz ścieżkę', justify='center',command=add_path)
path_button.place(relheight=1, relwidth=0.3)

path_entry = tk.Entry(frame_path, )
path_entry.place(relheight=1, relwidth=0.7, relx=0.3)

open_button =tk.Button(root,text='Otwórz plik',command=open_file) # open button
open_button.place(relx=0.4,rely=0.2)

frame_parse = tk.Frame(root)  # frame for parsing
frame_parse.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.4)

parse_button = tk.Button(frame_parse, text='XML działaj', justify='center',command=parse_XML)
parse_button.place(relheight=1, relwidth=0.4)


root.mainloop()# keep as the last line