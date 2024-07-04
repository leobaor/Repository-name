import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename()  # Abre el cuadro de diálogo para seleccionar el archivo
    return file_path

selected_file = select_file()
if selected_file:
    print(f'Selected file: {selected_file}')
    # with open(selected_file, 'r') as file:
    #     content = file.read()
else:
    print("No file selected.")

file_path = selected_file

with open(file_path, 'rb') as file:  # Abrir el archivo PDF en modo binario
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"Page {page_num + 1}:\n{text}\n")
