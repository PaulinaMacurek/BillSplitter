import random

class BillSplitter:

    friends_dictionary = {}
    number_of_friends = 0
    bill = 0
    lucky_feature = False
    lucy_one = None

    def __init__(self):
        print('Enter the number of friends joining (including you):')
        self.number_of_friends = int(input())

    def check_is_anyone(self):
        if self.number_of_friends > 0:
            return True
        else:
            print('\nNo one is joining for the party')
            return False

    def friends_input(self):
        print('\nEnter the name of every friend (including you), each on a new line:')
        self.friends_dictionary = {input(): 0 for _ in range(self.number_of_friends)}

    def lucky_feature_quest(self):
        print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        self.lucky_feature = True if input() == "Yes" else False
        self.lucky_feature_fun()

    def lucky_feature_fun(self):
        if self.lucky_feature:
            self.lucy_one = random.choice(list(self.friends_dictionary.keys()))
            print(f"\n{self.lucy_one} is the lucky one!")
        else:
            print("\nNo one is going to be lucky")

    def take_bill(self):
        print('\nEnter the total bill value:')
        self.bill = float(input())

    def split_bill(self):
        split_bill = self.bill/self.number_of_friends if not self.lucky_feature else self.bill/(self.number_of_friends-1)
        split_bill = round(split_bill, 2)
        self.friends_dictionary = {key: split_bill for key in self.friends_dictionary.keys() if key != self.lucy_one}
        if self.lucky_feature:
            self.friends_dictionary[self.lucy_one] = 0



moj = BillSplitter()

if moj.check_is_anyone():
    moj.friends_input()
    moj.take_bill()
    moj.lucky_feature_quest()
    moj.split_bill()
    print(moj.friends_dictionary)
else:
    pass