def solution(numbers, target):
    answer = 0
    n = len(numbers)
    counts=[numbers]
    def count(i):
        plus = numbers[:n-i]
        if i == 1:
            for count in counts[:]:
                print('plus', plus+[(-1)*numbers[n-i]])
                counts.append(plus + [(-1)*numbers[n-i]])

        else:
            for count in counts[:]:
                counts.append(plus + [(-1)*numbers[n-i]] + count[n-i+1:])
        print('counts', counts)
        
    for i in range(1,n+1):
        count(i)
    results = list(map(sum, counts))
    print('results', results)
    answer = results.count(target)
    print('answer', answer)
    return answer



solution([1,1,1,1,1], 3)