function solution(a, b) {
    return Math.max(Number(`${a}${b}`), 2*a*b)
}

function anotherSolution(a,b){
    let num1 = parseInt(a+""+b);
    let num2 = 2*b*a;
    return num1 > num2 ? num1 : num2
}


console.log(solution(2, 91))
console.log(solution(91,2))