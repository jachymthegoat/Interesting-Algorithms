def je_v_pohode(i, damy):
    for j in range(len(damy)):
        # ve stejnym radku jine sloupce nemuzou mit damu
        # rozdil mezi sloupcem a radkem musi byt stejny pro obe diagonaly
        if damy[j] == i or abs(damy[j] - i) == len(damy) - j:
            return False
    return True

def reseni(queens, n=4):
    if len(queens) == n:
        print(queens)
        return
    for i in range(n):
        if je_v_pohode(i, queens):
            reseni(queens + [i])

reseni([])