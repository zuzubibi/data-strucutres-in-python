// Set
// 고유값을 관리할 때 좋은 컬렉션
// 자료형에 관계없이 유일한 값을 저장

const members = [
    {
        name : 'kim',
        age : '30',
        hobby : 'game'
    },
    {
        name : 'kwon',
        age : '31',
        hobby : 'reading books'
    },
    {
        name : 'park',
        age : '29',
        hobby : 'sleeping'
    },
    {
        name : 'kong',
        age : '26',
        hobby : 'game'
    },
]

const hobby = members.reduce((acc, cur) => {
    return acc.add(cur.hobby)
}, new Set());

console.log(hobby);