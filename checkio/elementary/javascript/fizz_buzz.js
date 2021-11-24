function fizzBuzz(data) {
    if (data % 3 == 0 && data % 5 == 0){
        return "Fizz Buzz"
    } else if (data % 3 == 0) {
        return "Fizz"
    } else if (data % 5 == 0) {
        return "Buzz"
    } else {
        return `${data}`
    }
}

// data = (data % 3 === 0 && data % 5 === 0) ? "Fizz Buzz":
//     (data % 3 === 0) ? "Fizz" :
//     (data % 5 === 0) ? "Buzz" : data.toString();
// return data;


console.log(fizzBuzz(15)) //, "Fizz Buzz", "15 is divisible by 3 and 5");
console.log(fizzBuzz(6)) //, "Fizz", "6 is divisible by 3");
console.log(fizzBuzz(5)) //, "Buzz", "5 is divisible by 5");
console.log(fizzBuzz(7)) //, "7", "7 is not divisible by 3 or 5");
