function sort(arr: number[]) {
    return arr.sort((a, b) => a - b);
}

function cari_kucing_pendek(
    n: number,
    p: number,
    tinggi_kucing: number[]
): number {
    // Your code starts here.
    tinggi_kucing = sort(tinggi_kucing);
    return tinggi_kucing[p - 1];
}

export default cari_kucing_pendek;
