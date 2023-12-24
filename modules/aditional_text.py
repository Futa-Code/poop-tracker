import pandas as pd

def aditional_text():
    df = pd.read_csv(f'raw-data/poop-tracker.csv')

    with open('processed-data/text/aditional_text.txt', 'w', encoding='utf-8') as text_file:
        for _, row in df.iterrows():
            adicional = row['Acontecimientos del dia o texto adicional (OPCIONAL)']
            if isinstance(adicional , str):
                text_file.write(adicional + '\n')