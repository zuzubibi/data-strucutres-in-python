// 내 답
input = ['abcde'];

// for (var i = 0; i < input[0].length; i++){
//     console.log(input[0][i]);
// }


// 인상적인 답 1
str = input[0];
[...str].forEach( c=> console.log(c));


// 인상적인 답 2
// str = input[0];
// for(let i of str){
//     console.log(i);
// }