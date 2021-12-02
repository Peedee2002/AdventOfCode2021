import { calculateIncreased, openNumberFile, makeWindowArray } from "./day1_funcs.mjs";


const windowArray = makeWindowArray(openNumberFile('./input1.in'));

console.log(calculateIncreased(windowArray).reduce((a, b) => a + b));