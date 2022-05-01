# Huruf Mutu

def hurufMutu(nilai):
    if nilai >= 76:
        return ("A")
    elif nilai >= 71 and nilai < 76:
        return ("B+")
    elif nilai >= 66 and nilai < 71:
        return ("B")
    elif nilai >= 61 and nilai < 66:
        return ("C+")
    elif nilai >= 56 and nilai < 61:
        return ("C")
    elif nilai >= 50 and nilai < 56:
        return ("D")
    else:
        return ("E")

n = int(input())
nilai = []

for i in range(n):
    nilai.append(int(input()))

for i in nilai:
    print(f"{i} {hurufMutu(i)}")