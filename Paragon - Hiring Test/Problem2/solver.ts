function faktorBilangan(bilangan: number): number[] {
    const faktor: number[] = [];
    for (let i = 0; i <= bilangan; i++) {
        if (bilangan % i == 0) {
            faktor.push(i);
        }
    }
    return faktor;
}

function cari_agak_prima(n: number): string {
    const faktor: number[] = faktorBilangan(n);
    if (faktor.length <= 4) {
        return "YA";
    }

    return "BUKAN";
}

export default cari_agak_prima;
