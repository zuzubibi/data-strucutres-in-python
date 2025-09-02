// https://school.programmers.co.kr/learn/courses/30/lessons/42839

function getPermutation(arr, length) {
    if (length === 1) return arr.map(item => [item]);

    const result = [];
    arr.forEach((fixed, idx, self) => {
        const rest = [...self.slice(0, idx), ...self.slice(idx + 1)];
        const perms = getPermutation(rest, length - 1);
        const attached = perms.map(perm => [fixed, ...perm]);
        result.push(...attached);
    });
    return result;
}

function solution(numbers) {
    const arr = numbers.split('');
    const seen = new Set();

    // 1자리 ~ n자리 순열
    for (let len = 1; len <= arr.length; len++) {
        const perms = getPermutation(arr, len);
        console.log('?', perms);
    }
}

console.log('solution', solution("17")) // 3 (7, 17, 71)
console.log('solution2', solution("011")) // 2 (11, 1)
