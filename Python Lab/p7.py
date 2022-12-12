# Names
# import re
# file = open('textone.txt','r')
# text = file.read()
# pattern = r'M\w*\.\s*\w*'
# names = re.findall(pattern,text)
# print(names)

# Email
# import re
# file = open('textthree.txt','r')
# text = file.read()
# pattern = r'[0-9a-zA-Z\.\-+_]+@[0-9a-zA-Z\.\-+_]+\.[a-zA-Z]+'
# names = re.findall(pattern,text)
# print(names)

# Email extraction
# import re
# file = open('textthree.txt','r')
# text = file.read()
# x = re.findall(r'\S+.@',text)
# y = re.findall(r'@\S+.',text)
# for i,j in zip(x,y):
#     print("User id: ", i[:-1], "\nDomain : ", j[1:])

# URL
# import re
# file = open('texttwo.txt','r')
# text = file.read()
# pattern = r'\b(www|plus)[.][a-zA-Z0-9]+([.]com\b|[.]ac[.]in\b|[.]co[.]in\b)'
# names = re.finditer(pattern,str(text))
# for i in names:
#     print(i)

# Numbers
# import re
# file = open('textfour.txt','r')
# text = file.read()
# pattern = r'\d{8}|\d{3,5}.\d{2,4}.\d{2,6}'
# names = re.findall(pattern,text)
# for i in names:
#     print(i)

import re
file = open('textfour.txt','r')
text = file.read()
pattern = r'[7-9][0-9]{9}'
names = re.findall(pattern,text)
for i in names:
    print(i)
