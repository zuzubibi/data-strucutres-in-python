// map(): 형태를 바꿀 수 있지만 길이는 유지
// sort(): 정렬) 순서만 바꿈 (형태나 길이는 변경 안됨)
// filter(): 필터) 원하는 기준에 따라 길이 변경 (형태를 변경하지 않음)
// find(): 필터) 한 개의 데이터를 찾음 (형태를 변경하지 않음)
// forEach(): 반복) 형태를 이용해 반복작업을 함. 반환값 없음
// reduce(): 무엇이든 가능 (길이와 형태를 바꾸거나 새로운 데이터를 만들 수 있다.)

const carData = [
    {"id":1,"제조사":"Divape","이름":"Creedland"},
    {"id":2,"제조사":"Demizz","이름":"Treacher"},
    {"id":3,"제조사":"Eazzy","이름":"Kelner"},
    {"id":4,"제조사":"Twitterbeat","이름":"Fermoy"},
    {"id":5,"제조사":"Browsedrive","이름":"Burnham"},
    {"id":6,"제조사":"Centizu","이름":"Fraczkiewicz"},
    {"id":7,"제조사":"Miboo","이름":"Shakle"},
    {"id":8,"제조사":"Topicshots","이름":"Bernardi"},
    {"id":9,"제조사":"Trunyx","이름":"Jeanet"},
    {"id":10,"제조사":"Jaloo","이름":"Chasmar"}
]


// sort()
const copied = [...carData];
// console.log(copied.sort((a,b) => a.name - b.name))


// map()
const manufacturer = copied.map(item => {
    return item.제조사
});
// console.log(manufacturer);

// filter()
const filtered = manufacturer.filter(man => man.length >= 6);
// console.log(filtered);

// 합체
const filter = [...carData]
    .sort((a,b) => (a.id - b.id))
        .map(item => item.제조사)
        .filter(man => man.length >= 6);

// console.log(filter);


// find()
// console.log(carData.find(car => car.제조사 === 'Miboo'));
// console.log(carData.find(car => car.제조사 === 'Ru') || '결과값 없음');


// forEach()
// function getId(item) {
//     console.log(item.id);
// }
// carData.filter(car => car.제조사.length >= 6)
//     .forEach(item => getId(item))



// reduce()
const Data = [
    {"id":1,"name":"Tabbie Meaddowcroft","city":"Meaddowcroft"},
    {"id":2,"name":"Madelle Leopard","city":"Leopard"},
    {"id":3,"name":"Nan McNerlin","city":"McNerlin"},
    {"id":4,"name":"Tildie Henningham","city":"Henningham"},
    {"id":5,"name":"Zebulon Douse","city":"Douse"},
    {"id":6,"name":"Moses Coenraets","city":"Coenraets"},
    {"id":7,"name":"Joly Guihen","city":"Guihen"},
    {"id":8,"name":"Corie Bocken","city":"Bocken"},
    {"id":9,"name":"Carley Jordeson","city":"Jordeson"},
    {"id":10,"name":"Merrill Tonner","city":"Tonner"},
    {"id":11,"name":"Rosalynd McTerry","city":"McTerry"},
    {"id":12,"name":"Anastasie Kampshell","city":"Kampshell"},
    {"id":13,"name":"Dario McCrachen","city":"McCrachen"},
    {"id":14,"name":"Shirlee Heinritz","city":"Heinritz"},
    {"id":15,"name":"Otha Capaldo","city":"Capaldo"}
]

const init = [];
const callback = (acc, cur) => {
    if (cur.id >= 10) {
        return [...acc, cur]
    }
    return [...acc]
}

const applied = Data.reduce(callback, init);

// console.log(applied);

const favorite = [
    {"name":"Darcy Cockney","color":"violet"},
    {"name":"Llewellyn Ayllett","color":"red"},
    {"name":"Gardie Haxby","color":"green"},
    {"name":"Valeria Omand","color":"blue"},
    {"name":"Tan Kolyagin","color":"skyblue"},
    {"name":"Simona Urlich","color":"yellow"},
    {"name":"Alan Maling","color":"wihte"},
    {"name":"Melonie Cissen","color":"black"},
    {"name":"Pietrek MacHoste","color":"black"},
    {"name":"Celeste Jakes","color":"white"},
    {"name":"Basil Thiolier","color":"green"},
    {"name":"Ashlen Keyson","color":"red"},
    {"name":"Buddie Bulfoy","color":"red"},
    {"name":"Dodie Berndtsson","color":"white"},
    {"name":"Milzie Mammatt","color":"violet"}
]

const reduced = favorite.reduce((acc, cur) => {
    const count = acc[cur.color] || 0
    return {
        ...acc, [cur.color]: count+1
    }
}, {})
console.log(reduced);
