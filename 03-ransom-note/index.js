var canConstruct = function (ransomNote, magazine) {
    let hash = new Map()
    let found = true
    magazine.split('').forEach(char => {
        if (hash.has(char))
            hash.set(char, hash.get(char) + 1)
        else
            hash.set(char, 1)
    });
    ransomNote.split('').forEach(char => {
        if (hash.has(char)) {
            hash.set(char, hash.get(char) - 1)
            if (hash.get(char) < 0)
                found = false
        } else
            found = false
    })
    return found
}

var canConstruct2 = function(ransomNote, magazine) {
    for(let i=0;i<ransomNote.length;i++){
        let rem = magazine.replace(ransomNote[i],"");
        if(rem===magazine){
            return false;
        }
        console.log(rem)
        magazine = rem;
    }
    return true;
};


console.log(canConstruct2('aaac', 'aabaca'))