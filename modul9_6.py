def all_variants(text):
    x = len(text)
    for i in range(x):
        for j in range(i + 1, x + 1):
            yield text[i:j]

a = all_variants("abc")
for i in a:
    print(i)
