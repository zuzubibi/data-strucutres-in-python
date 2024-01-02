// 1. 함수: 특정 기능을 수행하는 코드의 단위
// 즉, 코드 여러 줄이 모여 있는 코드 모음이다.
// 이 코드 모음은 반드시 1개 이상의 목적이 있어야 합니다.
function sumNumbers(a,b){
    return a+b;
}

sumNumbers(10,20)  //30

// 2. 함수 표현식과 함수 선언문
// javaScript는 다른 프로그래밍 언어와 달리 함수 선언 방법이 2가지 있다

// 함수 표현식
var sumNumbers = function(a,b){
    return a+b;
}

// 함수 선언문
function sumNumbers(a,b){
    return a+b;
}

// 함수 표현식과 같이 함수를 정의할 수 있는 이유: 일급 객체(first class citizens)
// 일급 객체: 함수도 변수나 인자처럼 취급할 수 있기 때문


// 3. 함수형 사고와 함수형 프로그래밍
// 함수 작성할 때 단일 책임 원칙(single responsibility principle)을 지켜주면 좋다
// 단일 책임 원칙: 1개 함수에 1개의 기능만 담당해야 한다는 프로그래밍 원칙
// 함수에 여러 기능이 있으면 재사용하기 어렵고 이는 Vue.js 컴포넌트를 설계할 때도 사고 방식에 영향을 준다.

// 단일 책임 원칙에 벗어나는 코드
function sumNumbers(a,b){
    var num = 1000;
    var data = {};

    $.get('domain.com/products/1').then(function(response){
        data = response.data;
    });

    var total = a + b + num;
    return total
}

// 함수 리펙토링
function sumNumbers(a,b){
    return a+b;
}

function sumAll(){
    var num = 1000;
    var total = sumNumbers(0,0) + num;
    return total;
}

function fetchData(){
    var data = {};
    $.get('domain.com/products/1').then(function(response){
        data = response.data;
        return data;
    });
}

// 함수형 프로그래밍을 하기 위해서는 클로져(closure)라는 개념을 정확히 이해해야함
