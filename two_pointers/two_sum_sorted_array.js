// Naive solution already did in two sum
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twosum = function(numbers, target) {
    const map = new map()

    for(let i = 0; i < numbers.length; i++) {
        const diff =  target - numbers[i]
        if(map.has(numbers[i])){
            return [map.get(numbers[i]) + 1, i + 1]
        } else {
            map.set(diff,i)
        }
    }
};


// We will take advantage of sorted array mentioned in the question
// 
var twosumtwo = function(numbers, target) {
    let l = 0
    let r = numbers.length - 1

    while (l < r){
        if(numbers[l] + numbers[r] === target){
            return [l+1, r+1]
        }else if (numbers[l] + numbers[r] < target){
            l = l+1

        }else if (numbers[l] + numbers[r] > target){
            r = r - 1
        }
    }
};

console.log(twosumtwo( [-1,0], -1))
