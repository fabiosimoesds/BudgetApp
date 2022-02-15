class Category:

    def __init__(self, category):
        self.category = category.lower()
        self.ledger = list()


    def deposit(self, amount, description=''):
        dep = dict()
        dep['amount'] = amount
        dep['description'] = description
        self.ledger.append(dep)



    def withdraw(self, amount, description=''):
        check = Category.check_funds(self, amount)

        if check is True:
            withd = dict()
            withd['amount'] = amount*-1
            withd['description'] = description
            self.ledger.append(withd)
            return True

    def get_balance(self):
        sum_values = 0
        for value in self.ledger:
            sum_values += value['amount']
        return sum_values


    def transfer(self, amount, another_category):
        check = Category.check_funds(self, amount)

        if check is True:
            trans = dict()
            trans['amount'] = amount
            trans['description'] = f'Transfer from {self.category}'
            another_category.ledger.append(trans)
            trans_wit = dict()
            trans_wit['amount'] = amount*-1
            trans_wit['description'] = f'Transfer to {another_category.category}'
            self.ledger.append(trans_wit)
            return True



    def check_funds(self, amount):
        sum_values = 0
        for value in self.ledger:
            sum_values += value['amount']
        if sum_values < amount:
            return False
        else:
            return True

    def format(self):
        print(f'{self.category.title():*^30}')
        for value in self.ledger:
            amount = str(f'{value["amount"]:.2f}')
            print(f'{value["description"][:23]:<23}{amount:>7}')
        sum_values = 0
        for value in self.ledger:
            sum_values += value['amount']
        print(f'Total: {sum_values}')

    def __str__(self):
        return str(Category.format(self))


def create_spend_chart(categories):
    print('hi')


