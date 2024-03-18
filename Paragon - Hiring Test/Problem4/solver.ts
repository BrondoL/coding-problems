function mengintip_kucing(n: number, tinggi_kucing: number[]): number {
    // Your code starts here.
    let result: number = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i - 1; j >= 0; j--) {
            if (tinggi_kucing[j] <= tinggi_kucing[i]) {
                result++;
            } else {
                break;
            }
        }
        result++;
    }

    return result;
}

export default mengintip_kucing;
