import subprocess
import os

folder_path = r'ready_cut_code'
sciezka_do_programu = r"ready_emekaer_wp.py"

files_in_folder = os.listdir(folder_path)
txt_files = [file for file in files_in_folder if file.endswith('.txt')]

for i in range(0, len(txt_files), 4):   #it depend from number of cores on your procesor
    batch_files = txt_files[i:i+4]  
    processes = []
    for file_name in batch_files:   
        file_path = os.path.join(folder_path, file_name)
        process = subprocess.Popen(["python", sciezka_do_programu, file_path])
        processes.append(process)

    
    for process in processes:
        process.wait()
