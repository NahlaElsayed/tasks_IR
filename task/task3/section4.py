my_dict={'1':'nahla',
            '2':'elsayed'
            }
print(my_dict)
print(type(my_dict))

def my_index(k,m):
      return k%m
m=3
print(f'the hash value 1 is={my_index(1,m)}')
print(f'the hash value 2 is={my_index(2,m)}')
print(f'the hash value 3 is={my_index(3,m)}')
