licznik = 0
l2 = 0
dzielnik = 1000
max_lines = 893673501 // dzielnik  

with open(r'combinations.txt', 'r', encoding='utf-8', errors='ignore') as infile:
    outfile = open(fr'ready_cut_code\{l2}.txt', 'w', encoding='utf-8', errors='ignore')

    for line in infile:
        outfile.write(line)
        licznik += 1

        if licznik == max_lines:
            outfile.close()
            licznik = 0
            l2 += 1
            outfile = open(fr'ready_cut_code\{l2}.txt', 'a', encoding='utf-8', errors='ignore')  #record 1000 files to folder

        if l2 == dzielnik:
            break

    outfile.close()  # division for 1000 files 
