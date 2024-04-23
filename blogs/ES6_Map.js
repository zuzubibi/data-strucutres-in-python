const Data = {
    1 : {
        name : 'kwon',
        age : '31',
        gender : 'male'
    },
    2: {
        name : 'doson',
        age : '30',
        gender : 'male'
    },
    3: {
        name : 'kong',
        age : '26',
        gender : 'female'
    }
}

const entry = Object.entries(Data);
const aMap = new Map(entry);
console.log(aMap);

for (let record of aMap) {
    console.log(record);
}

aMap.forEach((item, key) => {
    console.log(`${key} : ${item.name}`)
})

console.log(aMap.get('1'));

console.log(aMap.entries());
console.log(aMap.keys());
console.log(aMap.values());

const aArray = Array.from(aMap);
console.log(aArray);
const modified = [...aArray];
console.log(modified);

const reducerApplied = modified.reduce((acc, cur) => {
    return {
        ...acc,
        [cur[0]]: cur[1]
    }
},{})
console.log(reducerApplied);