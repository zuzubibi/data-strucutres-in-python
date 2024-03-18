// 내 답

function solution(ineq, eq, n, m){
    if(ineq =='>' && eq =='='){
        return Number(n >= m)
    }else if (ineq =='<' && eq == '='){
        return Number(n <= m)
    }else if (ineq == '>' && eq == '!'){
        return Number(n > m)
    }else if (ineq == '<' && eq == '!'){
        return Number(n < m)
    }
}

// 다른 사람 답
const operations = {
    ">=" : (n,m) => n >=m,
    "<=" : (n,m) => n <=m,
    ">!" : (n,m) => n >m,
    "<!" : (n,m) => n <m
};

function anotherSolution(ineq, eq, n,m){
    const op = operations[ineq+eq];
    return Number(op(n,m));
}

console.log(solution("<", "=", 20,50)) //1
console.log(anotherSolution(">", "!", 41, 78)) //0