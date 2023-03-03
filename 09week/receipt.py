import csv
def main():
    KEY_INDEX = 0

    products_dict = read_dictionary("09week/products.csv", KEY_INDEX)
    print('All Products')
    print(products_dict)

    request = []
    with open('09week/request.csv', 'rt') as request_file:
        reader = csv.reader(request_file)
        next(reader)
        for item in reader:
            # clean_line = item.strip()
            request.append(item)
    print()
    print('Requested Items')
    for items in request:
        request = items[0]
        # print(request)
        products = products_dict[request]
        product_name = products[1]
        product_price = products[2]
        quantity = items[1]
        print(f'{product_name}: {quantity} @ {product_price}')

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
    with open(filename, 'rt') as products_file:

        reader = csv.reader(products_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

if __name__ == '__main__':
    main()