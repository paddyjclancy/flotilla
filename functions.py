import csv

def read_flotilla():
    with open('flotilla.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def new_entry():
    print('Plant ID:')
    id = input()
    print('Plant species:')
    species = input()
    print('Country of origin:')
    origin = input()
    print('[IMAGE?]')
    image = input()
    print('Water Frequency:')
    water_freq = input()
    print('Light Requirements:')
    light_req = input()
    print('Last known repot:')
    repot = input()
    print('Any notes?')
    notes = input()
    new_data = [id,species,origin,image,water_freq,light_req,repot,notes]
    append_flotilla(new_data)

def append_flotilla(data):
    with open('flotilla.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        f.close()