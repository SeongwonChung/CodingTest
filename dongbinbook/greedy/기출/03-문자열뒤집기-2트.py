import sys

s = sys.stdin.readline().rstrip()
change = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        change += 1

print(round(change / 2))


##정석풀이
"""전부 0으로 바꾸는 경우, 전부 1로 바꾸는 경우 모두 계산해보고 적은것이 정답!"""

data = input()
count0 = 0
count1 = 0

if data[0] == "1":
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == "1":
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))