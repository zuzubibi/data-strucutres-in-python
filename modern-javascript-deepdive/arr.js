/*
push() : 배열에 데이터 추가 (맨 끝)
slice() : 배열의 특정 인덱스에 있는 값을 반환(내용 변경 x)
splice() : 배열의 특정 인덱스에 있는 값을 변경 또는 삭제 (배열의 내용이 변경됨)
pop() : 배열의 마지막 인덱스의 값을 꺼냄 (배열의 내용이 변경)
shift() : 배열의 첫번째 인덱스의 값을 꺼냄 (배열의 내용이 변경)
*/

var arr = [];
arr.push(100);
arr.push(20);
arr.splice(0,1,10);
console.log(arr);

console.log(arr.shift());
const a = arr.shift();
console.log(arr);
console.log(a);

