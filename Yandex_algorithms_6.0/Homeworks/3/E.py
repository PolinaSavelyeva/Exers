from collections import deque


def from_infix_to_postfix(infix_expr):
    ans = []
    opers = deque()

    def helper(excl_opers, cur_oper):
        while len(opers):
            popped = opers.pop()
            if popped in excl_opers:
                opers.append(popped)
                break
            else:
                ans.append(popped)
        opers.append(cur_oper)

    for char in infix_expr:
        if char.isdigit():
            ans.append(char)
        elif char == '+':
            helper(['('], '+')
        elif char == '-':
            helper(['('], '-')
        elif char == '*':
            helper(['(', '+', '-'], '*')
        elif char == '(':
            opers.append('(')
        elif char == ')':
            while len(opers):
                popped = opers.pop()
                if popped == '(':
                    break
                else:
                    ans.append(popped)
        else:
            return "WRONG"
    for i in reversed(opers):
        ans.append(i)
    return ans


def eval_expr(postfix_expr):
    stack = deque()
    for char in postfix_expr:
        if char.isdigit():
            stack.append(char)
        elif len(stack) < 2:
            return "WRONG"
        elif char == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif char == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif char == '-':
            snd = int(stack.pop())
            fst = int(stack.pop())
            stack.append(fst - snd)
        else:
            return "WRONG"
    if len(stack) != 1:
        return "WRONG"
    return int(stack.pop())


def parse_str(str):
    i = j = 0
    input = []
    while i < len(str):
        while j < len(str) and str[j].isdigit():
            j += 1
        if i != j:
            if str[i:j].replace(" ", "") != "":
                input.append(str[i:j])
            i = j
        else:
            if str[i].replace(" ", "") != "":
                input.append(str[i])
            i += 1
            j = i
    return input


def check_braces(inp):
    i = 0
    for j in inp:
        if i < 0:
            return "WRONG"
        elif j == '(':
            i += 1
        elif j == ')':
            i -= 1
    if i < 0:
        return "WRONG"
    return inp


# if input[0] == '-':
#     input.insert(0, '0')
# for i in range(len(input)):
#     if input[i] == '(':
#         if input[i+1]


str = input()
print(from_infix_to_postfix(check_braces(parse_str(str))))
print(eval_expr(from_infix_to_postfix(check_braces(parse_str(str)))))
