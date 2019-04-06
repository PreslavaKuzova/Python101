import csv
from operator import itemgetter
def filter(file_name, **kwargs):    
    result = []
    
    with open('data.csv', mode = 'r') as csv_file:
        data = csv.DictReader(csv_file)    
        for row in data:
            flag = True
            order = False
            index_to_order_by = ''         
            for key, value in kwargs.items():
                key_word, sep, condition = key.partition('__')
                
                if condition != '':
                    if condition == 'startswith':
                        if not row[key_word].startswith(value):
                            flag = False
                    if condition == 'contains':
                        if not value in row[key_word]:
                            flag = False
                    if condition == 'gt':
                        if not int(value) < int(row[key_word]):
                            flag = False
                    if condition == 'lt':
                        if not int(value) > int(row[key_word]):
                            flag = False
                else:
                    if key_word == 'order_by':
                        order = True
                        index_to_order_by = ['full_name', 'favourite_color', 'company_name', 'email', 'phone_number', 'salary'].index(value)
                        continue
                    if row[key_word] != value:
                        flag = False

            if flag:
                result.append(list(row.values()))
        if order:
            return sorted(result, key=itemgetter(index_to_order_by))
    return result
    

def main():
    print(filter('data.csv', full_name="Diana Harris", favourite_color="lime"))
    print(filter('data.csv', full_name__startswith="Gary"))
    print(filter('data.csv', email__contains="@gmail"))
    print(filter('data.csv', salary__gt=9930))
    print(filter('example_data.csv', salary__lt=700, order_by='salary'))

if __name__ == '__main__':
    main()