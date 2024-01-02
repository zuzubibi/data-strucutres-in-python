// JavaScript는 프로토타입 기반 언어 입니다.
// 프로토타입 기반 언어: 어떤 객체를 원형(prototype)으로 삼고 이를 참조함으로써
// 상속과 비슷한 효과를 얻는다.

var simpleArray = new Array();
console.log(Array.prototype === simpleArray.__proto__); // True

// 1. prototype chain
// 1-1. 메서드 오버라이드
function Person(name) {
    this.name = name;
  }

Person.prototype.printName = function(){
    console.log(this.name);
}

var ironMan = new Person("Tony Stark");

//printName 메서드 오버라이드
ironMan.printName = function(){
    console.log(`I am ${this.name}`);
}

ironMan.printName();


// 위 예제는 ironMan 인스턴스에 printName 메서드를 다시 정의했다.
// 실행 결과를 보면, ironMan.__proto__.printName이 아닌, ironMan 객체에 있는 printName 메서드가 호출되었다.
// 위와 같은 현상을 '메서드 오버라이드' 라고 한다. 메서드 위에 메서드를 덮어씌웠다는 표현
// 자바스크립트 엔진이 printName이라는 메서드를 찾는 방식은 먼저 실행 컨텍스트의 속성을 검색하고,
// 존재하지 않는다면 __proto__를 순차적으로 검색하는 순서로 진행하기 때문에 ironMan 객체에 있는
// printName 메서드가 호출되었다.

// 1-2. 프로토타입 체이닝
// 메서드 오버라이드에 대해 알아보았으니 맨 처음으로 돌아가 Array를 사용하는 예제를 다시 보자
var simpleArray = new Array(1,2); // [1,2]
simpleArray.push(3); //[1,2,3]
simpleArray.hasOwnProperty(2); // true
// 정의하지 않은 push, hasOwnProperty 함수를 사용할 수 있는 이유는 자바스크립트 엔진이 메서드를 
// 찾는 방식이 먼저 자신의 속성을 확인하고, 존재하지 않는다면 그 다음으로 가까운 대상인 __proto__를 
// 검색하는 순서로 진행하기 때문이다.


// 프로토타입 체인: 어떤 데이터의 __proto__ 속성 내부에 다시 __proto__속성이 연쇄적으로 이어진 것
// 프로토타입 체이닝: 이 체인을 계속 따라가며 검색하는 것