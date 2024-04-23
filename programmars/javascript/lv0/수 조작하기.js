// 정답 다시 써보기

const operations = {
    w: (n) => n+1,
    s: (n) => n-1,
    d: (n) => n+10,
    a: (n) => n-10,
};

function solution(n, control){
    return [...control].reduce((prev, op) => operations[op](prev), n);
}



const control = "wsdawsdassw";
const n = 0;
console.log(solution(n, control));