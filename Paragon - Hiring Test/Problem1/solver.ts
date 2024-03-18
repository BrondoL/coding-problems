function rotasi_matriks(n: number, m: number, matrik: number[][]): number[][] {
    // Your code starts here.
    const result: number[][] = [];

    for (let i = 0; i < m; i++) {
        const arr: number[] = [];
        for (let j = n - 1; j >= 0; j--) {
            arr.push(matrik[j][i]);
        }
        result.push(arr);
    }

    return result;
}

export default rotasi_matriks;
