function validParentheses(s: string): string {
    // Your code starts here.
    const stack: string[] = [];

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (char === "[") {
            stack.push("]");
        } else if (char !== stack.pop()) {
            return "salah";
        }
    }

    if (stack.length === 0) {
        return "benar";
    }

    return "salah";
}

export default validParentheses;
