function anotherSolution(num_list){
    let accMul = 1
    let accSum = 0
    for (const num of num_list){
        accMul *= num
        accSum += num
    }  
    return accMul < accSum ** 2 ? 1 : 0
}

function anotherSolution2(num_list){
    let mul = num_list.reduce((a,c) => {return a*c ;}, 1);
    let sum = num_list.reduce((a,c) => {return a+c ;}, 0);
    return (mul < sum * sum) ? 1: 0;
}

console.log(anotherSolution([3, 4, 5, 2, 1])) //1
console.log(anotherSolution2([5, 7, 8, 3]))  //0