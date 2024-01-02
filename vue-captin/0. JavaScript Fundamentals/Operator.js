// 연산자의 활용 1 - 변수 초기화

// 일반적인 변수 초기화
function fetchData(data){
    var receiveData;
    if (data === undefined){
        receiveData = localStorage.getItem('item');
    }
}


// 논리 연산자를 사용한 변수 초기화
function fetchData(data){
    var receiveData;
    receiveData = data || localStorage.getItem('item');
}



// 연산자의 활용 2 - 조건문 대신 삼항 연산자
// if문을 중첩 사용하는 경우가 많음
if (data !== undefined){
    num = 50;
    if (num > 10){
        num = 100;
    }else{
        num = 0;
    }
}

// if문 대신 삼항 연산자를 쓰면 더 간결한 코드가 가능하다
if (data !== undefined){
    num = 50;
    num = num >10? 100: 0;
}