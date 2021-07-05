import sys, os
from json_to_text import *

# HOW TO USE
# python3 lang8_to_text.py [filename1] [filename2] ...
# or python3 lang8_to_text.py folder [foldername]

def save_txt(file_name):
    # make if checklist do not exist
    make_checklist()

    # check if already read
    if is_read(file_name):
        return
     
    # convert lang8 to text
    with open(file_name) as file:
        with open('corr.txt', 'a') as corr_file:
            with open('incorr.txt', 'a') as incorr_file:
                lines = file.readlines()
                corr_data, incorr_data = [], []
                for line in lines:
                    words = line.split('\t')

                    # has wrong word
                    if len(words) >= 6:
                        corr_data.append(words[5].strip())
                        incorr_data.append(words[4].strip())
                

                for line in corr_data:
                    corr_file.write(line + '\n')
                for line in incorr_data:
                    incorr_file.write(line + '\n')
            
    
    # add to checklist
    add_to_checklist(file_name)

if __name__ == '__main__':
    print(sys.argv[1:])
    
    # folder mode
    if sys.argv[1] == 'folder':
        cwd = os.getcwd()
        only_files = [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
        for file_name in only_files:
            print(file_name)
            save_txt(file_name)

    # file mode
    for file_name in sys.argv[1:]:
        save_txt(file_name)
        