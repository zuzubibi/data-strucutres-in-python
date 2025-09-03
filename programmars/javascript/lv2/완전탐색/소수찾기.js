// https://school.programmers.co.kr/learn/courses/30/lessons/42839
/* 
문제 핵심: 순열 만들기 + 소수인지 판별
공부 날짜: 2025.09.03(수)
*/

function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) {
        if (n % i === 0) return false;
    }
    return true;
}

// length 자리 수만큼 arr로 순열만들기
function getPermutation(arr, length) {
    if (length === 1) return arr.map(item => [item]); // 재귀 함수의 탈출 조건문

    const result = [];
    arr.forEach((fixed, idx, self) => {
        const rest = [...self.slice(0, idx), ...self.slice(idx + 1)]; // 현재 idx기준 양옆의 숫자들을 남김
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
        perms.forEach(p => {
            const num_str = p.join('').replace(/^0+|0+$/g, ''); // 양쪽 0 제거
            if (!num_str) return;
            const num = parseInt(num_str);
            if (isPrime(num)) seen.add(num);
        })
        console.log('?', len, perms);
        console.log('result >', seen);
    }
    return seen.size;
}

console.log('solution', solution("17")) // 3 (7, 17, 71)
console.log('solution2', solution("011")) // 2 (11, 1)
