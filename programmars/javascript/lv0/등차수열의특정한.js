function anotherSolution(a,d,included){
    return included.reduce((acc, flag, i) => {
        return flag ? acc + a + d * i : acc
    }, 0)
}

function anotherSolution2(a,d,included){
    var answer = 0;
    //an = a + (n-1)d;
    for (let i =0; i < included.length; i ++){
        if(included[i]){
            answer += (a + (d*i))
        }
    }
    return answer;
}

function solution(a,d,included){
    let answer =0
    let ex = 0
    for (let i = 0 ; i <included.length; i +=1){
        if (included[i]){
            ex = a + d*i
            answer += ex
        }
    }
    return answer
}

console.log(solution(3,4,[true, false, false, true, true])) //37
console.log(anotherSolution(7,1,[false, false, false, true, false, false, false])) //10
