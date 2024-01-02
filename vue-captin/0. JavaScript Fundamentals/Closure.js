// 1. 클로져(Closure)
// 함수의 실행이 끝난 뒤에도 함수에 선언된 변수의 값을 접근할 수 있는
// 자바스크립트의 성질
// 다른 언어와 비교했을 때 차별화되는 유일한 특징이다.

function addCounter(){
    var counter = 0;

    return function() {
        return counter++;
    };
}

var add = addCounter();
add(); // 0
add(); // 1
add(); // 2

// 위와 같이 동작하는 이유는
// "add 변수가 addCounter()가 반환한 함수를 참조하고 있다" 때문

// 이처럼 함수의 실행이 끝나고 나서도 함수 안의 변수를 참조할 수 있는게 바로
// 클로져입니다. 이러한 패턴을 응용하면 private 변수를 만들거나 함수형 
// 프로그래밍을 할 수 있습니다.



// 2. private 변수
// 일반적으로 프로그래밍에서 외부에서 사용하지 않거나 접근하면 안 되는 
// 변수와 함수는 private로 선언하여 사용합니다.

// 클로져를 활용해 private 변수를 구현하는 방법
var fund = (function(){
    var money = 0;
    return {
        deposit: function(amount){
            money += amount;
        },
        withdraw: function(amount){
            money -= amount;
        },
        getMoney: function(){
            return money;
        }
    }
}());

fund.deposit(100);  // 100
fund.deposit(100);  // 200
fund.getMoney();    // 200
fund.money = 100000; // private 변수로 변경되지 않는다.
fund.getMoney();    // 200


// 위 코드에서 호출된 함수 내부의 money 변수는 함수 내에서 제공한 deposit,
// withdraw, getMoney를 사용하는 것 외에 접근하는 방법이 없습니다.
// 이렇게 클로져를 사용하면 외부에서 변수에 직접 접근하는 것을 제한하는
// private 변수를 구현할 수 있습니다.



// 3. 함수형 프로그래밍
// 특정 기능을 구현하기 위해 함수의 내부 로직은 변경하지 않은 상태로 여러 개의
// 함수를 조합하여 결과 값을 도출하는 프로그래밍 패턴을 의미합니다.
// 커링(currying)이 함수형 프로그래밍의 대표적인 예입니다.

function add(num1, num2){
    return num1 + num2;
}

function curry(fn, a){
    return function(b){
        return fn(a,b);
    };
}

var add3 = curry(add, 3);
add3(4); //7