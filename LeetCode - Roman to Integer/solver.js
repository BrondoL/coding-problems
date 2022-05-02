/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    const symbols = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };
    let total = 0;

    let tmp = 1001;
    for (const x of s) {
        let num = symbols[x];
        if (tmp < num) {
            total += num - tmp * 2;
        } else {
            total += num;
        }
        tmp = num;
    }

    return total;
};
