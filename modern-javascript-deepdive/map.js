const map = new Map([['key1', 'val1'], ['key2', 'val2']]);

map.forEach((val, key) => {
    console.log(val + ','+ key);
});


for (let key of map.keys()){
    console.log(key);
}

for (let val of map.values()){
    console.log(val);
}

for (let[key, val] of map.entries()){
    console.log(key, val);
}

console.log(map.size)
console.log(map.has('key1'))
console.log(map.get('key2'))
map.delete('key2')
console.log(map)