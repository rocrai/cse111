import random
def main():
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers {numbers}')
    append_random_numbers(numbers)
    print(f'numbers {numbers}')
    append_random_numbers(numbers, 3)
    print(f'numbers {numbers}')

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        x = random.uniform(0,100)
        x = round(x,1)
        numbers_list.append(x)

if __name__ == '__main__':
    main()