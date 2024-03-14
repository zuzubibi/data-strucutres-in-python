input = [100]
input2 = [1]

// 인상적인 답: 삼항연산자
n = Number(input2[0]);
const result = n % 2 ? 'odd' : 'even'
console.log( n, 'is', result);


// 인상적인 답 2
console.log(n%2 == 0 ? `${n} is even`: `${n} is odd`)