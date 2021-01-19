"""
빠르게 입력 받기 🍯tip

이진탐색의 경우 입력데이터의 개수가 1000만개를 넘어갈 정도로 많은 경우가 많다. 이 경우, `sys` 라이브러리를 사용하여 빠르게 입력받을 수 있다.
"""

import sys
input_line = sys.stdin.readline().rstrip()
# readline()을 통해 한줄의 문자열을 읽는다. 줄바꿈을 '\n'으로 인식하므로, rstrip()으로 제거해준다.

print(input_line)