lan = ['c+', 'java', 'c#', 'python', 'javascript']

uri = 'c:/pythontxt/'
with open(uri + 'languages.txt', 'a') as f:
   f.writelines(lan)
