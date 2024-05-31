import modules.process as p
import modules.aditional_text as add

if __name__ == "__main__":
    path = 'raw-data/poop-tracker.csv'
    name_list = ['Tomas', 'Ram', 'Santiago']
    
    for name in name_list:
        p.process(name, path)
        add.aditional_text(name, path)
        