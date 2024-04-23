import modules.fun_fact as fun
import random
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

def choose_names(name_list, amount) -> tuple:
    names = []
    for i in range(amount):
        name = random.choice(name_list)
        name_list.remove(name)
        names.append(name)
        
    return names

def conversation(name_list, characters):
    names = choose_names(name_list, characters)
    
    dialogue = random.randint(5, 10)
    
    intro = f'Conversacion Futa entre {names[0]}'
    for i in range(1, characters - 1):
        intro += f', {names[i]}'
    intro += f' y {names[characters - 1]}:\n'
    
    delay_print(intro)
    for i in range(dialogue):
        row = fun.get_random_csv_row(f'processed-data/poops/{names[i%characters]}-poop.csv')
        delay_print(f'{names[i%characters]}: {row['Adicional']}\n')

if __name__ == "__main__":
    name_list = ['Tomas', 'Ram', 'Santiago']
    
    try:
        conversation(name_list, 2)
    except KeyboardInterrupt:
        print('\n~~~~~~~~~~~~~~\nImpaciente mi amigo\n~~~~~~~~~~~~~~\n')


