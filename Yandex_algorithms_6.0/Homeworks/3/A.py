from collections import deque


def correct_brackets_seq(brackets_seq):
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    stack_brackets = deque()
    for bracket in brackets_seq:
        if bracket in brackets_dict:
            stack_brackets.append(bracket)
        elif not len(stack_brackets) or bracket != brackets_dict.get(stack_brackets.pop()):
            print("no")
            return
    if len(stack_brackets):
        print("no")
        return
    print("yes")


input_brackets = input()
correct_brackets_seq(input_brackets)
