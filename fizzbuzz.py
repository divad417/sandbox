rules = {3: 'Fizz',
         5: 'Buzz'}

for i in range(1, 101):
    out = ''
    for key, value in rules.items():
        if i % key == 0:
            out += value
    if not out:
        out = i
    print(out)