// 1. this
// 함수 실행 컨텍스트를 가리키는 예약어
// 실행 컨텍스란, 사전적 정의로 '함수가 실행되는 환경'이며
// 쉽게 접근하자면, '함수가 실행될 때의 컨텍스트'로 이해하면 좋다.

// 2. 첫 번째 this
console.log(this); //window

// this의 가장 기본적 컨텍스트는 글로벌(전역) 컨텍스트이다.
// window는 자바스크립트의 최상위 객체를 가리킨다.



// 3. 두 번째 this
var obj = {
    num : 10,
    printNum: function(){
        console.log(this.num);
    }
};

obj.printNum(); //10

// 객체 속성 안의 this는 기본적으로 해당 객체를 가리킨다.


// 4. 세 번째 this

// 일반 함수(함수 선언문)에서의 this  -> 전역 컨텐스트(window)
function showComment(){
    console.log(this);
}

showComment(); //window

// 생성자 함수의 this -> 함수 내부를 가리킴
function Developer(){
    console.log(this);
}

var dev = new Developer(); // Developer {}

// 저렇게 나온 이유: new로 인스턴스 생성하는 순간 함수가 실행되기 때문



// 5. 네 번째 this
// 실제 웹 개발시 많이 마주하는 this
// 바로 데이터를 받아올 때 사용하는 HTTP 요청과 같은 비동기 처리 코드이다.
function fetchData() {
    axios.get('domain.com/products').then(function(){
        console.log(this);
    });
}

fetchData(); //window


// tip: 자바스크립트는 프로토타입 기반 언어이다.
// 클래스 기반 언어가 아니기 때문에 위와 같이 함수를 이용해 인스턴스를 생성할 수 있다.