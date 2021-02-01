s = input()

comp = [s[0]]
for n in s:
    if n != comp[-1]:
        comp.append(n)

zero = comp.count("0")
one = comp.count("1")

print(min(zero, one))