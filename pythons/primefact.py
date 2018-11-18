ntd = 13195
div = 2
factors = [1]

while True:
    r = ntd % div
    if r == 0:
        ntd = ntd/div
        factors.append(div)
        div = 2
    else:
        div = div+1
    if ntd == 1:
        break

print(factors)
