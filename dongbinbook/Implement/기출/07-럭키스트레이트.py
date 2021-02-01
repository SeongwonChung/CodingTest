n = input()
split = len(n) // 2
left = n[:split]
right = n[split:]

left = sum(map(int, left))
right = sum(map(int, right))

print(left, right)
if left == right:
    print("LUCKY")
else:
    print("READY")
