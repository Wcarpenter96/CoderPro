var reconstructQueue = function (people) {
    console.log(people)
    people.sort((a, b) => b[0] - a[0])
    res = []
    people.forEach(p => {
       res.splice(p[1],0, p) 
    });
    return res
};

// const compare = ([h1, k1], [h2, k2]) => {
//     if (h1 !== h2) return h2 - h1;
//     else return k1 - k2;
//   };
//   people.sort(compare);

console.log(reconstructQueue(
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
))