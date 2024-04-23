// map 객체 복사하기
const init = [['one', 'one'], ['two', 'two']];


// 참조에 의한 복사
const firstMap = new Map(init);
// const secondMap = firstMap;

// secondMap.set('one', '1');
console.log(firstMap);


// 해결방법
const secondMap = new Map([...firstMap]); // 펼침연산자
secondMap.set('one', '1');
console.log(firstMap);


// 객체 리터럴
const inited = {
    one: 'one',
    two: 'two'
};
const second = {...inited};
second.one = '1';

console.log(inited);



const initData = {
    one:'one',
    two:'two',
    three : {
        one:'one',
        two:'two'
    }
}

const _ = require('lodash');
const copy = _.cloneDeep(initData);
copy.three.one = '1';
console.log(initData);

const copy_shallow = {...initData};
copy_shallow.three.one = '1';
console.log(initData);


