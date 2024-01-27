licznik = 0
l2 = 0
dzielnik = 1000
max_lines = 893673501 // dzielnik  

with open(r'C:\tmp\filter_all_combinations.txt', 'r', encoding='utf-8', errors='ignore') as infile:
    outfile = open(fr'C:\tmp\ready_cut_code\{l2}.txt', 'w', encoding='utf-8', errors='ignore')

    for line in infile:
        outfile.write(line)
        licznik += 1

        if licznik == max_lines:
            outfile.close()
            licznik = 0
            l2 += 1
            outfile = open(fr'C:\tmp\ready_cut_code\{l2}.txt', 'a', encoding='utf-8', errors='ignore')

        if l2 == dzielnik:
            break

    outfile.close()  # Zamknięcie ostatniego pliku, jeśli nie osiągnięto warunku l2 == dzielnik
