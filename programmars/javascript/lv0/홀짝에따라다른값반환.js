function solution(n){
    sum = 0
    if (n %2 ==0){
        for (let i = 0; i<=n;i++){
            if (i%2==0){
                sum += i*i
            }
        }
    }else{
        for (let i = 1; i<=n;i++){
            if (i%2==1){
                sum += i
            }
        }
    }
    return sum
}

function anotherSolution(n){
    if (n%2==1){
        return (n+1)/2 *((n+1)/2)
    }else{
        return n *(n+1)*(n+2)/6
    }
}

console.log(anotherSolution(7))
console.log(anotherSolution(10))