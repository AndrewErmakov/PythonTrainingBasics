import re


def check_DOM_string(sentence):
    opening_tags = ['<b>', '<i>', '<div>', '<e>', '<p>']
    closing_tags = ['</b>', '</i>', '</div>', '</e>', '</p>']

    stack = []

    tags_list = re.split('(<[^>]*>)', sentence)[1::2]

    for tag in tags_list:
        if tag in opening_tags:
            stack.append(tag)
        elif tag in closing_tags:
            pos = closing_tags.index(tag)
            if (len(stack) > 0) and (opening_tags[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                continue
    if stack:
        return stack[-1].replace('<', '').replace('>', '')
    return True


print(check_DOM_string(input()))
