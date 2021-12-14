closers = {
    '}' : '{',
    ')' : '(',
    ']' : '[',
    '>' : '<' 
}
illegals = {
    '}' : 0,
    ')' : 0,
    ']' : 0,
    '>' : 0
}

values = {
    '{' : 3,
    '(' : 1,
    '[' : 2,
    '<' : 4
}

def calculateIncompleteScore(stack):
    score = 0
    for value in reversed(stack):
        if value == 'failed':
            return 0
        score *= 5
        score += values[value]
    return score

def removeAllZeros(list):
    try:
        while True:
            list.remove(0)
    except ValueError:
        return list

if __name__ == '__main__':
    scores = []
    for line in open('input.in'):
        stack = []
        for value in line[:-1]:
            if value in closers.keys():
                if len(stack) == 0 or stack[-1] != closers[value]:
                    illegals[value] += 1
                    stack.append('failed')
                    break
                stack.pop()
            else:
                stack.append(value)
        scores.append(calculateIncompleteScore(stack))


    print(illegals['}'] * 1197 + 57 * illegals[']'] + illegals[')'] * 3 + illegals['>'] * 25137)
    print([*sorted(removeAllZeros(scores))][int(len(scores) / 2)])