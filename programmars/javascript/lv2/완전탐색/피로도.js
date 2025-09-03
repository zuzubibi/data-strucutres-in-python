// https://school.programmers.co.kr/learn/courses/30/lessons/87946
/* 
문제 핵심: 순열 (완전탐색)
공부 날짜: 2025.09.03(수요일)
*/

function getPermutation(arr, length) {
    if (length === 1) return arr.map(item => [item]);

    const result = [];
    arr.forEach((fixed, idx, self) => {
        const rest = [...self.slice(0, idx +1), ...self.slice(idx + 1)];
        const perms = getPermutation(rest, length - 1);
        const attached = perms.map(perm => [fixed, ...perm]);
        result.push(...attached);
    })
    return result;
}
function solution(k, dungeons) {
    const list = getPermutation(dungeons, dungeons.length);

    let max_count = 0;
    list.forEach(item => {
        let count = 0;
        let fatigue = k;
        for ([need, cost] of item) {
            if (fatigue >= need) {
                fatigue -= cost;
                count ++;
            } else {
                break;
            }
        }
        max_count = Math.max(max_count, count);
    })
    return max_count;
}


console.log('result >', solution(80, [[80,20],[50,40],[30,10]])) // 3