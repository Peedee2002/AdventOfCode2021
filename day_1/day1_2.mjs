import { calculateIncreased, openNumberFile, makeWindowArray } from "./day1_funcs.mjs";

console.log(calculateIncreased(makeWindowArray(openNumberFile('./input1.in'))));
