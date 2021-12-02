import { readFileSync } from 'fs';


export const openNumberFile = (fileName) => {
    const file = readFileSync(fileName, "utf-8");
    const lines = file.split(/\r?\n/);
    return lines.map((value) => parseInt(value));
} 


export const calculateIncreased = (lines) => lines.map((line, index) => {
    if (index === 0) return 0;
    return line > lines[index - 1] ? 1 : 0;
})

export const makeWindowArray = (array) => {
    const window = array.map((value, index) => {
        if (index === 0 || index === array.length - 1) return NaN;
        return value + array[index - 1] + array[index + 1];
    })
    return window.filter((value) => !isNaN(value));
}
