def solution(name):
    def topDown(answer,c):
        answer += min((ord(c) - 65, 90-ord(c)+1))
        return answer
    def leftRight(wordToChange, name, i):
        moveR=1
        moveL=1
        #right
        while True:            
            if i+moveR > len(name)-1:
                indexR = i+moveR - len(name)
            else: 
                indexR = i+moveR
            if wordToChange[indexR] != name[indexR]:
                break
            moveR+=1
        #left
        while True:            
            if i-moveL < 0:
                indexL = i-moveL + len(name)
            else: 
                indexL = i-moveL
            if wordToChange[indexL] != name[indexL]:
                break
            moveL+=1
        
        if moveR <= moveL:
            return moveR, indexR
        else:
            return moveL, indexL
        
    answer = 0
    cursor = 0
    wordToChange = ['A']*len(name)
    name=list(name)
    #topDown
    for c in name:
        answer = topDown(answer, c)
    #leftRight
    while wordToChange != name:
        print('cursor', cursor)
        print('wordToChange', wordToChange)
        print('name', name)
        #change first letter
        wordToChange[cursor] = name[cursor]
        #start move
        move, cursor = leftRight(wordToChange, name, cursor)
        print('move', move)
        wordToChange[cursor] = name[cursor]
        answer+= move
    print('answer: ', answer)
    return answer

solution('BBAAAABBB')