import modules.fun_fact as fun
from datetime import datetime
import random

if __name__ == "__main__":
    name_list = ['Tomas', 'Ram', 'Santiago']
    name = random.choice(name_list)

    row = fun.get_random_csv_row(f'processed-data/poops/{name}-poop.csv')

    try:
        # Convertir la cadena de fecha a objeto datetime
        fecha = datetime.strptime(row['Fecha'], "%Y-%m-%d")

        # Obtener el dato curioso
        dato_curioso = fun.obtener_dato_curioso(fecha)

        # Imprimir el resultado
        if row['Adicional'] == "":
            print(f'En la fecha {row['Fecha']}, {name} hizo un sorete\nDato curioso: {dato_curioso}')
        else:    
            print(f'En la fecha {row['Fecha']}, {name} hizo un sorete y dijo "{row['Adicional']}"\nDato curioso: {dato_curioso}')

    except ValueError:
        print('Formato de fecha incorrecto. Utiliza el formato YYYY-MM-DD.')

