// Scope란 변수의 유효 범위를 의미합니다.

// 1. 글로벌 스코프
// 다른 프로그래밍 언어와 달리 자바스크립트의 변수는 유효 범위가 전역으로 시작한다.
var a = 10;

function getA(){
    console.log(a);
}

getA(); // 10


// 2. 로컬 스코프
// 기본적으로 변수의 유효 범위는 전역 범위를 갖는다지만, 함수 안에 새로 선언시
// 함수 단위의 지역 범위인 함수 스코프를 갖는다.

var a = 10;

function getA(){
    var a = 20;
    console.log(a);
}

getA(); // 20
console.log(a); //10


// 3. 스코프 체인(Scope Chain)
// 변수를 찾을 때 먼저 자신이 속한 스코프에서 찾고 없으면 상위 스코프에서 찾는 현상

// 글로벌 스코프
var a = 10;

function outer(){
    //외부 함수 스코프
    var b = 20;

    function inner(){
        //로컬 함수 스코프
        var c = 30;
        console.log(a);
        console.log(b);
        console.log(c);
    }
    inner();
};

outer(); // 10, 20, 30


// 4. 렉시컬 스코프
// 자바스크립트는 함수를 어디서 선언하였는지에 따라서 상위 스코프를 결정하는
// 렉시컬 스코프(Lexical Scope) 규칙을 따른다.

// 글로벌 스코프
var a = 10;
var b = 20;
function getA(){
    var b = a;
    getB();
}

function getB(){
    // 로컬 함수 스코프
    console.log(b);
}

getB(); //20
getA(); //20


// 5. 다이나믹 스코프 (Dynamic Scope)
// 렉시컬 스코프와 반대 개념이다.
// 함수의 호출 위치에 따라 상위 스코프가 결정된다.
// 대표적인 예: 쉘 스크립트

// A = 10
// B = 20

// getA(){
//     B=$A
//     getB
// }

// getB(){
//     echo $B
// }

// getB //20
// getA //10