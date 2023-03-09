import csv
from datetime import datetime
def main():
    KEY_INDEX = 0
    try:
        products_dict = read_dictionary("products.csv", KEY_INDEX)
        current_date_and_time = datetime.now()
        print('Inkom Emporium')
        # print(products_dict)
        total_price = []
        request = []
        num_items = []
        with open('request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)
            for item in reader:
                # clean_line = item.strip()
                request.append(item)
        print()
        for items in request:
            request = items[0]
            # print(request)
            products = products_dict[request]
            product_name = products[1]
            product_price = products[2]
            quantity = items[1]
            quantity = float(quantity)
            product_price = float(product_price)
            total = product_price * quantity
            total_price.append(total)
            num_items.append(quantity)
            print(f'{product_name}: {quantity} @ {product_price}')
        # print(total_price)
        total_prices = sum(total_price)
        total_quantity = sum(num_items)
        sales_tax = total_prices * 0.06
        total_price_with_tax = sales_tax + total_prices
        print()
        # print(total_prices)
        # print(total_quantity)
        # print(total_price_with_tax)
        # print(sales_tax)
        print(f'Number of Items: {total_quantity:.0f}')
        print(f'Subtotal: {total_prices:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total_price_with_tax:.2f}')
        print()
        print('Thank you for shopping at the Inkom Emporium.')
        print(f'{current_date_and_time:%a %b  %d %H:%M:%S %Y}')
    except FileNotFoundError as not_found_err:
        print('Error: missing file') 
        print(not_found_err)
    except PermissionError as permission_err:
        print('Error: missing file') 
        print(permission_err)
    except KeyError as key_err:
        print()
        print('Error: unknown product ID in the request.csv file')
        print(key_err)
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