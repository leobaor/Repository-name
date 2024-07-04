import shutil
import os
import tkinter as tk
from tkinter import filedialog
import mimetypes

#Función para obtener la terminación del archivo basado en el tipo MIME
def obtener_terminacion(tipo_mime):
    if tipo_mime == 'application/pdf':
        return 'pdf'
    elif tipo_mime == 'text/plain':
        return 'txt'
    elif tipo_mime == 'image/jpeg':
        return 'jpg'
    elif tipo_mime == 'image/png':
        return 'png'
    elif tipo_mime == 'application/msword':
        return 'doc'
    elif tipo_mime == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return 'docx'
    else:
        return 'desconocido'


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
    
 
source_path = selected_file
mime_type, _ = mimetypes.guess_type(source_path)
terminacion = obtener_terminacion(mime_type)
destination_path = os.path.join(f"{os.getcwd()}\\destino.{terminacion}")

print(f'El tipo MIME del archivo es: {mime_type}')
print(destination_path)
try:
    shutil.copy2(source_path, destination_path)
    print(f'Archivo copiado de {source_path} a {destination_path}')
except FileNotFoundError:
    print(f'El archivo {source_path} no fue encontrado.')
except PermissionError:
    print(f'Permiso denegado para copiar el archivo a {destination_path}.')
except Exception as e:
    print(f'Ocurrió un error: {e}')