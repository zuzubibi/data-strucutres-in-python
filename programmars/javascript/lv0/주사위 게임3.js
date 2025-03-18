function count(arr) {
    const counter = new Map();
    for (const data of arr){
        counter.set(data, (counter.get(data) || 0 ) +1);
    }

    const sortedByCnt = [...counter.keys()].sort((a,b) => counter.get(b) - counter.get(a));
    const maxCnt = Math.max(...counter.values());

    return [sortedByCnt, maxCnt];
}
function solution(a,b,c,d) {
    const [arr, maxCnt] = count([a,b,c,d]);
    const [p,q,r,s] = arr;
    if (arr.length === 1) {
        return p * 1111;
    }
    if (arr.length === 2) {
        return maxCnt === 2 ? (p + q ) * Math.abs(p-q) : (10* p+q)**2;
    }
    if (arr.length === 3) {
        return q * r;
    }
    return Math.min(p,q,r,s);
}


console.log(solution(2,2,2,2))  // 2222
console.log(solution(4,1,4,4))  // 1681
console.log(solution(6,3,3,6))  // 27
console.log(solution(2,5,2,6))  // 30
console.log(solution(6,4,2,5))  // 2
