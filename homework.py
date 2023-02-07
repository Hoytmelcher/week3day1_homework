import re


with open('./names.txt') as g:
    data1 = g.readlines()


fullname = re.compile('([A-Z][a-zA-Z]+,) ([A-Z][a-zA-Z]+(-[A-Z][a-zA-Z]+)*)')

twitter = re.compile('(@[a-z]+)$')

for line in data1:
    display = twitter.search(line)
    display2 = fullname.search(line)
    if display:
        print('\n'f"{display2.group(2)} {display2.group(1)} / {display.group(1)}")
        










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
        
        










