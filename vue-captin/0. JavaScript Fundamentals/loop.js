// 1. forEach()
// 배열에 사용하기 좋은 반복문

var arr = [10,20,30];

arr.forEach(function(value, index){
    console.log('array index:', index, ' value : ', value);
});


// 2. for in 
// 배열과 객체 모두 사용하기 좋은 반복문
// vue의 v-for 디렉티브의 모티브가 되는 문법

var arr = [10,20,30];
var obj = {
    num: 10,
    str: 'hi',
    arr: [],
}

// 배열의 인덱스를 1개씩 접근하여 순차적으로 순회하는 경우
for (var key in arr){
    console.log(arr[key]);
}


// 객체의 키를 1개씩 접근하여 순차적으로 순회하는 경우
for (var key in obj){
    console.log(obj[key]);
}



// 3. for of
// ES6에 추가된 구문
// iterable 속성을 가지는 컬렉션에 사용하기 좋은 반복문

// iterable 속성은 두 조건을 만족합니다.
// 1) 객체가 [Symbol.iterator] 메서드를 가지고 있어야 합니다.
// 2) [Symbol.iterator] 메서드는 iterator 객체를 반환해야 합니다.

// 아래 예시) 반복 가능하지 않은 객체는 에러가 난다
// TypeError: obj is not iterable
var obj = {
    num: 10,
    str: 'hi',
    arr: [],
}

for (var prop of obj){
    console.log(prop, obj[prop]);
}


// 4. for of vs for in
var arr = [10,20,30]

// 배열을 각각 순회하는 경우

// for of: 객체의 열거 가능한 속성에 대해 반복
for (var num of arr){
    console.log(num);
}

// for in: 반복 가능한 속성을 가지는 컬렉션(Arrays, Objects, Map, ...)에 대한 반복
for (var num in arr){
    console.log(num);
}
