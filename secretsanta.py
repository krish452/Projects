import random
def en(my_list):
    list1 = my_list
    num = len(list1)
    final_dict = {}
    if num <= len(list1):
        random_values = random.sample(list1, num)
    final_dict = dict(zip(list1,random_values))
    return final_dict

def unique(my_dict):
    for key,value in my_dict.items():
        if key == value:
           other_pair = next((k, v) for k, v in my_dict.items() if k != value and v != key)
           my_dict[key], my_dict[other_pair[0]] = other_pair[1], key
    return my_dict 

def santa(dict_names):
    your_name = input('Enter your name \n')
    print(f'Woohooooo!!!! Your santa child is: {dict_names[your_name]}')
                

def main():
    name_list = []
    print('Note: Member 1 is the organizer of this group')
    num = int(input('Enter number of members in the group: \n'))
    for i in range(1,num+1):
        name = input(f'Member{i}: \n')
        name_list.append(name)
    val = en(name_list)
    result = unique(val)
    santa(result)
    character = input('View drawn names \n')
    organizer_name=name_list[0]
    if character == 'y' or character == 'Y':
        field = input('Enter your name \n')
        if field == organizer_name:
            print(result)
        else:
            print('Sorry, only the organizer can view this list.')
    else:
        print("Thank you using Kichu's secret santa generator")
main()