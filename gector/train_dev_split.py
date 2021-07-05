import sys, random

def train_dev_split(file_name, train_ratio):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        random.shuffle(lines)

        train_line = int(len(lines) * train_ratio)

        # write train.txt
        with open('train.txt', 'w') as train_file:
            for line in lines[:train_line]:
                train_file.write(line)
        
        # write dev.txt
        with open('dev.txt', 'w') as dev_file:
            for line in lines[train_line:]:
                dev_file.write(line)

        print(f'total : {len(lines)} lines')
        print(f'train.txt : {train_line} lines')
        print(f'dev.txt : {len(lines) - train_line} lines')


if __name__ == '__main__':
    file_name = sys.argv[1]
    train_ratio = float(sys.argv[2])

    train_dev_split(file_name, train_ratio)