import pandas as pd 
import re
from datetime import datetime

def create_csv(file_path, data, columns):
    try:
        # Create a DataFrame using pandas
        df = pd.DataFrame(data, columns=columns)

        # Write the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def parse_date(raw_date: tuple):
    date = raw_date[0]
    hour = raw_date[1]
    date = date[:-14]

    if isinstance(hour, str):
        date = re.sub(r"\d?\d:\d\d", hour, date)

    format = "%Y/%m/%d %H:%M"

    # Parse the string to create a datetime object
    parsed_date = datetime.strptime(date, format)
    return parsed_date

def process(name: str, path: str):
    df = pd.read_csv(path)

    columns = ['Fecha', "Hora", "Dureza", "Volumen", "Adicional"]
    data = []
    for _, row in df.iterrows():
        data_row = []
        if row['Nombre'] == name:
            date = parse_date((row['Marca temporal'], row['Hora']))
            data_row.append(date.date())
            data_row.append(date.strftime("%H:%M"))
            data_row.append(row['Dureza'])
            data_row.append(row['Volumen'])
            
            adicional = row['Acontecimientos del dia o texto adicional (OPCIONAL)']
            if isinstance(adicional, str):
                data_row.append(adicional)
            else:
                data_row.append("")

            data.append(data_row)
    create_csv(f'processed-data/poops/{name}-poop.csv', data, columns)
