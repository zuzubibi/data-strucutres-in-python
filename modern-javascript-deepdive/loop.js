// forEach()
var arr = [10,20,30];
arr.forEach(function(val, index) {
    console.log(index+':',val);
});

// for in 😉
var arr = [10,20,30];

var obj = {
    num: 10,
    str: 'hi',
    arr: [],
};


for (let i in arr){
    console.log(arr[i]);
}

for (let i in obj){
    console.log(obj[i]);
}

// for of 🥲

// ⭐️ 1) 이 코드는 에러가 난다  -> 객체는 iterable 하지 않음 
// for (let prop of arr){
//     console.log(prop, arr[prop]);
// }

//✅ 2) 방법 1 
for (let index of Object.keys(obj)){
    let val = obj[index];
    console.log(val, obj);
}

for (const [index, val] of Object.entries(obj)){
    console.log(val, obj);
}

//✅ 3) 방법 2
const md_obj = Object.entries(obj)
console.log(md_obj);
var map = new Map(md_obj);  // map은 iterable하다. ==> for of , forEach 사용 가능 ~!

for (let index of map.keys()){
    let val = map[index];
    console.log(val, index);
}

for (let val of map.values()) console.log(val);

for (const [key, val] of map.entries()) console.log(key, val);


console.log(map);
const aArray = Array.from(map);
console.log(aArray);

const modified = [...map];
console.log(modified);

const reducerApplied = modified.reduce((accum,current)=>{
    return {
        ...accum,
        [current[0]]:current[1]
    }
},{});

console.log(reducerApplied);