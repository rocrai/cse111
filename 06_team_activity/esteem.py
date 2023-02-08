def main():
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')
    print('')
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    score = 0
    answer = input('1. I feel that I am a person of worth, at least on an equal plane with others. \n   Enter D, d, a, or A: ')
    number = 1
    score = ans(answer, number, score)
    answer = input('2. I feel that I have a number of good qualities. \n   Enter D, d, a, or A: ')
    number = 2
    score = ans(answer,number, score)
    answer = input('3. All in all, I am inclined to feel that I am a failure. \n   Enter D, d, a, or A: ')
    number = 3
    score = ans(answer, number, score)
    answer = input('4. I am able to do things as well as most other people.  \n   Enter D, d, a, or A: ')
    number = 4
    score = ans(answer,number, score)
    answer = input('5. I feel I do not have much to be proud of.  \n   Enter D, d, a, or A: ')
    number = 5
    score = ans(answer,number, score)
    answer = input('6. I take a positive attitude toward myself.  \n   Enter D, d, a, or A: ')
    number = 6
    score = ans(answer,number, score)
    answer = input('7. On the whole, I am satisfied with myself.  \n   Enter D, d, a, or A: ')
    number = 7
    score = ans(answer,number, score)
    answer = input('8. I wish I could have more respect for myself.  \n   Enter D, d, a, or A: ')
    number = 8
    score = ans(answer,number, score)
    answer = input('9. I certainly feel useless at times.  \n   Enter D, d, a, or A: ')
    number = 9
    score = ans(answer,number, score)
    answer = input('10. At times I think I am no good at all.  \n   Enter D, d, a, or A: ')
    number = 10
    score = ans(answer,number, score)
    print('')
    print(f'Your score is {score}.')
    print('A score below 15 may indicate problematic low self-esteem.')

def ans(answer, number, score):
    if (number == 1 or number == 2 or number == 4 or number == 6 or number == 7) and answer == 'D':
        score = score + 0
    elif (number == 1 or number == 2 or number == 4 or number == 6 or number == 7) and answer == 'd':
        score = score + 1
    elif (number == 1 or number == 2 or number == 4 or number == 6 or number == 7) and answer == 'a':
        score = score + 2
    elif (number == 1 or number == 2 or number == 4 or number == 6 or number == 7) and answer == 'A':
        score = score + 3
    elif (number == 3 or number == 5 or number == 8 or number == 9 or number == 10) and answer == 'D':
        score = score + 3
    elif (number == 3 or number == 5 or number == 8 or number == 9 or number == 10) and answer == 'd':
        score = score + 2
    elif (number == 3 or number == 5 or number == 8 or number == 9 or number == 10) and answer == 'a':
        score = score + 1
    elif (number == 3 or number == 5 or number == 8 or number == 9 or number == 10) and answer == 'A':
        score = score + 0
    return score

main()