# Deskripsi Bilangan

deskripsi = ["satuan", "puluhan", "ratusan", "ribuan", "puluhribuan", "ratusribuan"]

n = input()
deskripsiBilangan = deskripsi[0:len(n)]
deskripsiBilangan = deskripsiBilangan[::-1]

for x in range(len(n)):
    print(f"{n[x]} {deskripsiBilangan[x]}")
