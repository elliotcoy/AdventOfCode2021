
# get input, each line a string in s[]
s = open('2021\D10\input.txt','r').read().splitlines()

out = 0

# count and score invalid brackets
for line in s:
    stack = ['.']
    for c in line:
        match c:
            case '(': stack.append('(')
            case '[': stack.append('[')
            case '{': stack.append('{')
            case '<': stack.append('<')
            
            case ')':
                if stack.pop() != '(':
                    out += 3
                    continue
            case ']':
                if stack.pop() != '[':
                    out += 57
                    continue
            case '}':
                if stack.pop() != '{':
                    out += 1197
                    continue
            case '>':
                if stack.pop() != '<':
                    out += 25137
                    continue

print(out)

