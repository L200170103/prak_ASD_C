#nomer1
import re
print("Nomer 1")
f = open('Indonesia.txt', 'r')
p = r'me[\w\.-]+'
string = re.findall(p, f.read())
print(string)
print ("-------------------------------------------------------------------------")

#nomer2
import re
print("Nomer 2")

f = open('Indonesia.txt', 'r')
p = r'di[\w\.-]+'
string = re.findall(p, f.read())
print(string)
print ("-------------------------------------------------------------------------")

#nomer3
import re
print("Nomer 3")

f = open('Indonesia.txt', 'r')
r = r'di\s[\w\.-]+'
string3 = re.findall(r, f.read())
print(string3)
print ("-------------------------------------------------------------------------")

#nomer4
import re
print("Nomer 4")

f = open('KEI.html', 'r')

teks = f.read()

strings = re.findall(r'title="([\w+]+)">', teks)
strings= re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
a = []
for i in strings:
    a.append((i[0], float(i[1])))

print(a)
