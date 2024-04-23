const convert = {
    '1': 'w',
    '-1': 's',
    '10': 'd',
    '-10': 'a',
};

function solution(numLog) {
    return numLog.slice(1).map((v,i) => {
        return convert[v - numLog[i]]
    }).join('')
}

const numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1];
console.log(solution(numLog));