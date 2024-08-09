initial_list = [10, 9, 1, 2, 8, 7, 3, 4, 6, 5]
print(f'initial  list:   {initial_list}')

modified_list = initial_list.copy()
modified_list.append(-1)
print(f'modified list 1: {modified_list}')

modified_list.extend([-2, -5, -7])
print(f'modified list 2: {modified_list}')

modified_list.insert(2, 9)
print(f'modified list 3: {modified_list}')

print(f'amount of 1: {modified_list.count(1)}')
print(f'amount of 9: {modified_list.count(9)}')
print(f'amount of -10: {modified_list.count(-10)}')
print(f'index of 7: {modified_list.index(7)}')

checklist = [-2, -10]
for item in checklist:
    if modified_list.count(item):
        print(f'the list contains {item}')
    else:
        print(f'the list does not contain {item}')
    
modified_list.sort()
print(f'sorted list: {modified_list}')

modified_list.reverse()
print(f'reverse sorted list: {modified_list}')
