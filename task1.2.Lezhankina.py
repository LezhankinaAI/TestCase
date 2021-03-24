lst = [['Alexey', 23], ['Inna', 26], ['Alex', 39], ['Jane', 37], ['Olga', 42]]
print('Hello! What are you interested in: the names of the group members or their ages? (Type "names" or "ages")')
work = True
while work:
    mode = input()
    if mode.lower() == "names":
        print("Names: ", end='')
        print(*[l[0] for l in sorted(lst, key=lambda x:x[0])], sep=', ', end='.')
        work = False
    elif mode.lower() == "ages":
        print("Ages: ", end='')
        print(*[l[1] for l in sorted(lst, key=lambda x:x[1])], sep=', ', end='.')
        work = False
    else:
        print('Please, choose again between "names" and "ages".')
