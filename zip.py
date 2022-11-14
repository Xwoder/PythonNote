a = ['w', 'x', 'y', 'z']
b = [1, 2, 3, 4, 5, 6, 7]
c = ['A', 'B', 'C']

r = zip(a, b, c)

for index, (first, second, third) in enumerate(r):
    print(f'index = {index}, '
          f'first = {first}, '
          f'second = {second}, '
          f'third = {third}')
