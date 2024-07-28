let input = document.querySelector("#input");
let result = document.querySelector(".result");
let btn = document.querySelector("button");

function calc(){
    //console.log(input.value);
    let num = eval(input.value);
    result.innerText = num;
};