import sys, json, os

# HOW TO USE
# python3 json_to_text.py [filename1] [filename2] ...
# or python3 json_to_text.py folder [foldername]

# make if checklist do not exist
def make_checklist():
    if not os.path.isfile('checklist.txt'):
        with open('checklist.txt', 'w') as file:
            pass

# check if already read
def is_read(file_name):
    with open('checklist.txt', 'r') as file:
        if (file_name + '\n') in file.readlines():
            print(file_name + ' already checked')
            return True
        else:
            return False

def add_to_checklist(file_name):
    with open('checklist.txt', 'a') as file:
        file.write(file_name + '\n')
        print(file_name + ' added successfully')

def save_txt(file_name):
    # make if checklist do not exist
    make_checklist()

    # check if already read
    if is_read(file_name):
        return
    
    # check json and edit if has error
    try:
        file = open(file_name)
        jsonString = json.load(file)
    except json.decoder.JSONDecodeError:
        with open(file_name, 'r') as file:
            whole_str = file.read()

            # add ',' every back of '}'
            whole_str = whole_str.replace('}', '},')

            # add '{"data":[', ']}' at the start & end of file
            whole_str = '{"data":[' + whole_str + ']}'

            # erase last ',')
            rindex = whole_str.rfind(',')
            whole_str = whole_str[:rindex] + whole_str[rindex+1:]

        # write file
        with open(file_name, 'w') as file:
            file.write(whole_str)
            file.close()
            print('except occured')
    
    # convert json to text
    with open(file_name) as file:
        dic = json.load(file)

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
        