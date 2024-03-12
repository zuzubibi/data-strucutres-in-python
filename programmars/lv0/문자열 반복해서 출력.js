const input = ['string', 5];
str = input[0];
n = Number(input[1]);

// 방법 1
console.log(str.repeat(n));

// 방법 2
for (let i=0; i < n; i++){
    process.stdout.write(str);
}
