class Bill:
    
    money_holder = {}

    def __init__(self, amount):
        self._validate_input_data(amount)
        self.amount = amount

        if self.amount in self.money_holder:
            self.money_holder[self.amount] += 1
        else:
            self.money_holder.update({self.amount : 1})

    def __str__(self):
        return 'A ${0} bill'.format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, value):
        return self.amount == value.amount

    def __repr__(self):
        return self.__str__()
        #if we run like __str__ it will return the default str method

    def __hash__(self):
        return super().__hash__()

    def _validate_input_data(self, amount):
        if not isinstance(amount, int):
            raise Exception('Type Error')
        if amount < 0:
            raise Exception('Value Error')

    def get_amount(self):
        return self.amount

class BillBatch():
    def __init__(self, bills):
        self.bills = bills
    
    def __len__(self):
        len = 0
        for b in self.bills:
            len += 1
        return len

    def total(self):
        sum = 0
        for bill in self.bills:
            sum += bill.get_amount()
        return sum

    def return_current_bill(self, index):
        return Bill(self.bills[index].get_amount())

class CashDesk():
    money = []

    def take_money(self, bills):
        if isinstance(bills, Bill):
            self.money.append(bills)
        else:
            for index in range(len(bills)):
                self.money.append(bills.return_current_bill(index))
    
    def desk_total(self):
        total_money = 0
        for bill in self.money:
            total_money += bill.get_amount()
        return total_money

    def inspect(self):
        print('We have a total of ${0} in the desk'.format(sum([bill.get_amount() for bill in self.money])))
        dic = {}
        for bill in self.money:
            if bill.get_amount() in dic:
                dic[bill.get_amount()] += 1
            else:
                dic.update({bill.get_amount(): 1})
        print(dic)

def main():
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)
    print(Bill.money_holder)
    lst = BillBatch([a, b, c])
    print(lst.total())
    
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]
    batch = BillBatch(bills)

    desk = CashDesk()
    desk.take_money(Bill(10))
    desk.take_money(batch)
    print(desk.desk_total())
    desk.inspect()
    

if __name__ == '__main__':
    main()