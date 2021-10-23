a = [(0, 'a'), (4, 'e')]
b = "apply"

for set in a:
    index = set[0]
    if set[1] == b[index]:
        is_matched = True
    else:
        is_matched = False
        break

print(is_matched)