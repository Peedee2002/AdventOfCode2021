import { calculateIncreased, openNumberFile } from "./day1_funcs.mjs";

const numbers = openNumberFile('./input1.in');

console.log(calculateIncreased(numbers).reduce((a, b) => a + b));
