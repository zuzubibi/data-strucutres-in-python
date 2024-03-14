// 내 답
function solution(str1, str2) {
    let result = '';
    for(let i = 0 ; i < str1.length; i++ ){
        result += str1[i];
        result += str2[i];
    }
    // console.log(result)
    return result
}


// 다른 사람 답
function anotherSolution(str1, str2){
    return [...str1].map((x, idx) => x + str2[idx]).join("");
}

const str1 = "aaaaa";
const str2 = "bbbbb";

console.log(solution(str1, str2))
