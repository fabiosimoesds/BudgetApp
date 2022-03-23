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
        else:
            return False

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
            trans['description'] = f'Transfer from {self.category.title()}'
            another_category.ledger.append(trans)
            trans_wit = dict()
            trans_wit['amount'] = amount*-1
            trans_wit['description'] = f'Transfer to {another_category.category.title()}'
            self.ledger.append(trans_wit)
            return True
        else:
            return False



    def check_funds(self, amount):
        sum_values = 0
        for value in self.ledger:
            sum_values += value['amount']
        if sum_values < amount:
            return False
        else:
            return True

    def format(self):
        listToConcat = list()
        listToConcat.append(f'{self.category.title():*^30}')
        sum_values = 0
        for value in self.ledger:
            sum_values += value['amount']
        for value in self.ledger:
            amount = str(f'{value["amount"]:.2f}')
            listToConcat.append(f'{value["description"][:23]:<23}{amount:>7}')
        listToConcat.append(f'Total: {sum_values}')
        prettyprint = ''
        for v in listToConcat:
            if 'Total' in v:
                prettyprint += v
            else:
                prettyprint += v+'\n'
        return prettyprint


    def __str__(self):
        return str(Category.format(self))


def create_spend_chart(categories):
    dic = dict()
    cat_name = list()
    for values in categories:
        tot = 0
        list_led = values.ledger
        cat = values.category.title()
        cat_name.append(cat)
        for index, values in enumerate(list_led):
            if list_led[index]['amount'] < 0:
                tot += float(list_led[index]['amount'])
                dic[cat] = tot
    total_spent = 0
    for keys, values in dic.items():
        total_spent += values
    dic_perc = dict()
    for keys, values in dic.items():
        dic_perc[keys] = int(values/total_spent*100//10*10)
    format_list = list()
    percent_list2 = list()
    format_list.insert(0, 'Percentage spent by category\n')
    for a in range(100, -10, -10):
        for keys, values in dic_perc.items():
            if values >= a:
                percent_list2.append('o  ')
            else:
                percent_list2.append('   ')
        format_list.append(f'{str(a) + "|":>4} {"".join(percent_list2[:])}\n')
        percent_list2.clear()

    print()
    format_list.append(f'    {"-"*3*len(dic_perc)}-\n')

    max_leng = max(map(len, cat_name))
    padded_cat = [item.ljust(max_leng, ' ')for item in cat_name]
    count = 0
    for row in zip(*padded_cat):
        if count < max_leng-1:
            format_list.append('     ')
            format_list.append(f'{"  ".join(row)}  \n')
            count += 1
        else:
            format_list.append('     ')
            format_list.append(f'{"  ".join(row)}  ')
    result_formated = ''.join(format_list)
    return result_formated






