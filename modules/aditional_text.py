import pandas as pd
import modules.process as process
                
def aditional_text(name, path):
    df = pd.read_csv(path)

    with open(f'processed-data/text/{name}_aditional_text.txt', 'w', encoding='utf-8') as text_file:
        for _, row in df.iterrows():
            adicional = row['Acontecimientos del dia o texto adicional (OPCIONAL)']
            if isinstance(adicional , str) and row['Nombre'] == name:
                text_file.write(adicional + '\n')