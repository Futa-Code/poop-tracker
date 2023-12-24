import requests
from googletrans import Translator
import csv
import random

def get_random_csv_row(file_path):
    try:
        # Read all rows from the CSV file
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            rows = []

            for row in csv_reader:
                if isinstance(row['Adicional'], str) and row['Adicional'] != '':
                    rows.append(row)

            # Check if there are any rows in the file
            if not rows:
                print(f"The CSV file '{file_path}' is empty.")
                return None

            # Select a random row
            random_row = random.choice(rows)

            return random_row

    except FileNotFoundError:
        print(f"Error: File not found at the specified path: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def traducir(texto):
    translator = Translator()
    translation = translator.translate(texto, src='en', dest='es')
    return translation.text

def obtener_dato_curioso(fecha):
    # Formatear la fecha en el formato MM/DD
    fecha_formato = fecha.strftime("%m/%d")

    # Hacer la solicitud a Numbers API
    url = f'http://numbersapi.com/{fecha_formato}/date'
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        dato_curioso = traducir(response.text)
        return dato_curioso
    else:
        return f'No se pudo obtener un dato curioso para la fecha {fecha}'

    
