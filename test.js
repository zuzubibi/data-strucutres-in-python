// const array = new Array(10).fill('test');

const example2 = [
    { id: 123, name: "nkh" },
    { id: 123, name: "ddd" },
    { id: 5456, name: "zxc" }
];
console.log([...new Set(example2.map(JSON.stringify))].map(JSON.parse));
// [{id: 123,  name: 'nkh'}, {id: 123, name: 'ddd'}, {id: 5456, name: 'zxc'}]
  

let example = [{ id: 123 }, { id: 456 }, { id: 123 }];
console.log([...new Set(example.map(JSON.stringify))].map(JSON.parse));