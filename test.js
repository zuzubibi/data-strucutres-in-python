todoList = [	
    {"completed":false,"item":"1","edit":false},
    {"completed":false,"item":"2","edit":false},
    {"completed":false,"item":"3","edit":false}
]

const itemList = todoList.map(item=>item.item);

console.log(itemList);

const newValue = '1';

if (!itemList.includes(newValue)){
    console.log('없습니다.');
}else{
    console.log('존재합니다.');
}
