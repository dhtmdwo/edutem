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
        with open('data.txt', 'a') as write_file:
            # write every text to data.txt
            for j in dic["data"]:
                text = j["text"]

                # correct the text
                index_add = 0
                for edit in j["edits"][0][1]:
                    if edit[2] is None:
                        text = text[:edit[0]+index_add] + text[edit[1]+index_add:]
                        index_add -= (edit[1] - edit[0])
                    else:
                        text = text[:edit[0]+index_add] + edit[2] + text[edit[1]+index_add:]
                        index_add += len(edit[2]) - (edit[1] - edit[0])
                
                write_file.write(text + '\n')
    
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
        