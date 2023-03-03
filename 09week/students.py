import csv
def main():
    pass
    KEY_INDEX = 0

    students_dict = read_dictionary("09week/students.csv", KEY_INDEX)

    
    student = input('Please enter an I-Number (xxxxxxxxx): ')
    if student in students_dict:
        student = students_dict[student]
        student = student[1]
        print(student)
    else:
        print('No such student')
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as students_file:

        reader = csv.reader(students_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

main()