function solution (my_string, index_list){
    // return index_list.map(i => my_string[i]).join('');
    return index_list.reduce((result, i) => result + my_string[i], '');
}

console.log(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7])) // "programmers"
console.log(solution("zpiaz", [1, 2, 0, 0, 3])) // "pizza"