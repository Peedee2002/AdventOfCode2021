# cant think of a clever general algo here
from itertools import permutations

def matchingLetters(str1, str2):
    return all((c in str1) for c in str2)

class TwoWayDict(dict):
    def __len__(self):
        return dict.__len__(self) / 2
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

if __name__ == '__main__':
    total = 0
    for line in open('input.in'):
        examples, displayed = line.split(' | ')
        examples = examples.split()
        displayed = displayed.split()
        answers = TwoWayDict()
        # determine 1, 4, 7, 8
        for example in examples:
            match (len(example)):
                case 2:
                    answers[example] = 1
                case 3:
                    answers[example] = 7
                case 4:
                    answers[example] = 4
                case 7:
                    answers[example] = 8

        # determine the 6, 9, 0
        len6 = (example for example in examples if len(example) == 6)
        for example in len6:
            if matchingLetters(example, answers[1]):
                answers[example] = 9 if matchingLetters(example, answers[4]) else 0
            else:
                answers[example] = 6
        
        # determine 2, 3, 5
        len5 = (example for example in examples if len(example) == 5)
        for example in len5:
            if matchingLetters(answers[9], example):    
                answers[example] = 3 if matchingLetters(example, answers[1]) else 5
            else:
                answers[example] = 2
        for index, display in enumerate(displayed):
            for perm in permutations(display):
                if ''.join(perm) in answers.keys():
                    displayed[index] = ''.join(perm)

        total += (int(''.join(str(answers[display]) for display in displayed)))
    print(total)