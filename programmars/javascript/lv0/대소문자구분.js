// 내가 쓴 답
str = 'aBcDeFg';
for (var attr in str){
    // console.log(attr);
    if (str[attr] === str[attr].toLowerCase()) {
        process.stdout.write(str[attr].toUpperCase());
    }else{
        process.stdout.write(str[attr].toLowerCase());
    }
}


// 다른 사람 답
// input = 'aBcDeFg';
// str = input.split('');
// str.forEach((value, index) => {
//     if (value === value.toUpperCase()) {
//         str[index] = value.toLowerCase();
//     } else {
//         str[index] = value.toUpperCase();
//     }
// });
// console.log(str.join(''));