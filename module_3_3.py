def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])
def print_params(a,b,c):
    print(a, b, c)
values_list = [2, 'word', False]
print_params(*values_list)
def print_params(a,b,c):
    print(a, b, c)
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)
def print_params(a,b,c):
    print(a, b, c)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)




