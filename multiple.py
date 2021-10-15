from Circut1loop import oneBinary

i = input()

il = list(i)
fl = []
for x in il:
    c = oneBinary(x)
    fl.append(c)
    pass

p = ' '.join(fl)

print(p)