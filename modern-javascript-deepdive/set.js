// const set = new Set();

// set.add('javascript').add('vue').add('node');
// console.log(set.has('vue'));

// set.delete('javascript');
// console.log(set);
// set.clear();
// console.log(set);

// set.forEach((val, val2, set) => {
//     console.log(val, val2, set);
// });

let s = new Set();
let set = new WeakSet();
key = {};
set.add(key);
set.add(key);
key = null;

console.log(key);
console.log(key);