#Program to return as few notes and coins as possible for an amount entered. 
import math
def dictionary_change(currency):
    minimum_notes = {'2000': int(currency)//2000, '500': int(currency)//500, '200': int(currency)//200, '100': int(currency)//100, '50':int(currency)//50, '20': int(currency)//20, '10': int(currency)//10}
    return minimum_notes

def coin_change(currency):
    if currency == .25:
        print('Number of 25 paise coin is:', currency//.25)
    elif currency == .50:
        print('Number of 50 paise coin is:', currency//.5)
    elif currency == .75:
        print('Number of 50 paise coin is:', currency//.5)
        currency -= .50
        print('Number of 25 paise coin:', currency//.25)
    else:
        print('Number of paise is 0.')

def coin_dispersal(currency):
    if currency < 5:
            if currency in [2,4]:
                print('Number of 2 rupee coins:', currency//2)
            elif currency == 1:
                print('Number of 1 rupee coin:', currency)
            else:
                print('Number of 2 rupee coin:', currency//2)
                print('Number of 1 rupee coin:', currency%2)
    elif currency > 5:
        print('Number of 5 rupee coin:', currency//5)
        if currency%5 in [2,4]:
            print('Number of 2 rupee coins:', (currency-5)//2)
        else:
            print('Number of 2 rupee coin:', (currency-5)//2)
            print('Number of 1 rupee coin:', (currency-5)%2)
    else:
        print('Number of 5 rupee coin:', currency//5)

def display_function(my_dict):
    for key, value in my_dict.items():
        print(f'Number of {key} notes is: {value}')

def minimum_val(minimum_notes):
    min_non_zero = float('inf')
    min_non_zero_key = None

    for key, value in minimum_notes.items():
        if value !=0 and value < min_non_zero:
            min_non_zero = value
            min_non_zero_key = key
    
    if min_non_zero_key is not None:
        return int(min_non_zero_key), min_non_zero
    else:
        return None, None
    
def convert_str_num(num):
    num_str = str(num)
    if '.' in num_str:
        num_str = num_str.replace('.', '')
    return (len(num_str))

def make_change():
    balance_list = {}
    currency = float(input('Enter amount:\n'))
    currency_frac, currency_whole = math.modf(currency)
    while (convert_str_num(currency_whole)>1):
        note_count = dictionary_change(currency_whole)
        value,count = minimum_val(note_count)
        if value is not None:
            currency_whole -= value*count
            balance_list[value] = count
        else:
            if currency_whole == 0:
                display_function(balance_list)
                coin_dispersal(currency_whole)
                coin_change(currency_frac)
                break
            else:
                display_function(balance_list)
                coin_dispersal(currency_whole)
                coin_change(currency_frac)
                break
make_change()
