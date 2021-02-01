import re

string = input()
eng = re.compile("[A-Z]")

a = []
n = 0
for c in string:
    if eng.match(c):
        a.append(c)
    else:
        n += int(c)
a.sort()

print("".join(a + [str(n)]))
