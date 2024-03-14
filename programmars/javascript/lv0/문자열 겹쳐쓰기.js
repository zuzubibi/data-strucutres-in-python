function solution(my_string, overwrite_string, s){
    n = my_string.slice(0,s) + overwrite_string
    m = n + my_string.slice(n.length)
    return m
}

function anotherSolution(my_string, overwrite_string, s){
    return my_string.slice(0,s) + overwrite_string + my_string.slice(s+overwrite_string.length);
}

console.log(anotherSolution("He11oWor1d", "lloWorl", 2, "HelloWorld"))
console.log(anotherSolution("Program29b8UYP", "merS123", 7, "ProgrammerS123"))