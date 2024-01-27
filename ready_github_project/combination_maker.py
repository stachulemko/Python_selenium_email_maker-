from itertools import product
from datetime import datetime


def generate_combinations(elements, output_file):
    combination_lengths = [1, 2, 3]

    with open(output_file, 'w', encoding='utf-8') as file:
        for length in combination_lengths:
            file.write(f"Kombinacje o długości {length}:\n")
            for combination in product(elements, repeat=length):
                combined = ''.join(str(elem) for elem in combination)
                file.write(f"{combined}\n")


def read_file_and_append_elements(file_path, elements):
    with open(file_path, 'rb') as file:
        for line in file:
            try:
                elements.append(line.strip().decode('utf-8'))
            except UnicodeDecodeError:
                pass


elements = []


file_paths = [
    r"C:\zapas_nowy\dev\attacks\ready_email\strings\ImionaMęskie.txt",
    r"C:\zapas_nowy\dev\attacks\ready_email\strings\ImionaŻeńskie.txt",
    r"C:\zapas_nowy\dev\attacks\ready_email\strings\NazwiskaMęskie.txt",
    r"C:\zapas_nowy\dev\attacks\ready_email\strings\NazwiskaŻeńskie.txt",
    r"C:\zapas_nowy\dev\attacks\ready_email\strings\słowa_polskie.txt",
    r"C:\zapas_nowy\dev\attacks\ready_email\strings\znaki.txt"
]


for file_path in file_paths:
    read_file_and_append_elements(file_path, elements)



generate_combinations(elements, 'combinations.txt')
