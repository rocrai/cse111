import csv
def main():
    text_list = read_list('09week/provinces.txt')

    print(text_list)

    text_list.pop(0)

    text_list.pop()
    
    for i in range(len(text_list)):
        if text_list[i] == 'AB':
            text_list[i] = 'Alberta'
    
    count = text_list.count('Alberta')
    print()
    print(f'Alberta occurs {count} times in the modified list.')

def read_list(filename):
    text_list = []

    with open(filename, "rt") as provinces_file:

        for line in provinces_file:

            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

if __name__ == '__main__':
    main()
