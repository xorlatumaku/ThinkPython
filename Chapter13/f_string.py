# Date: 06/11/2025
# Program to implement f-strings

num_years = 1.5
num_camels = 23

writer = open('camel-spotting-book.txt', 'w')
writer.write(str(num_years))
writer.write(str(num_camels))
writer.close()

open('camel-spotting-book.txt').read()
print(f'I have spotted {num_camels} camels')
print(f'In {num_years} years I have spotted {num_camels} camels')

line = f'In {round(num_years * 12)} months I have spotted {num_camels} camels'
print(line)
print()

writer = open('camel-spotting-book.txt', 'w')
writer.write(f'Years of observation: {num_years}\n')
writer.write(f'Camels spotted: {num_camels}\n')
writer.close()

data = open('camel-spotting-book.txt').read()
print(data)
