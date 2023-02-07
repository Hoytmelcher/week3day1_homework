import re

with open('./regex_test.txt') as f:
    data = f.readlines()
    print(data)

patern = re.compile('([A-J][a-z]+\sP|J[a-z]+\sA[a-z]+) ([G-W][a-z]+)')

patern2 = re.compile('([A-E][a-z]+) ([L-N][a-z]+)')



for famous in data:
    match = patern.search(famous)
    match2 = patern2.search(famous)
    if match:
        print('\n', f"{match.group(1)} {match.group(2)}")
    elif match2:
        print('\n', f"{match2.group(1)} {match2.group(2)}")
    else:
        print('None')
        
        










