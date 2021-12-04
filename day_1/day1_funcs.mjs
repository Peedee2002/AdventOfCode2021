import { readFileSync } from 'fs';


export const openNumberFile = (fileName) => {
    const file = readFileSync(fileName, "utf-8");
    const lines = file.split(/\r?\n/);
    return lines.map((value) => parseInt(value));
} 

export const calculateIncreased = (lines) => {
    if (lines.length === 1) return 0;
    return (lines[0] < lines[1] ? 1 : 0) + calculateIncreased(lines.slice(1));
}

export const makeWindowArray = (array) => {
    if (array.length < 3) return [];
    return [array[0] + array[1] + array[2]].concat(makeWindowArray(array.slice(1)))
}
