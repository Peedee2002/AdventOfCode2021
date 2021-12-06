use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("./../input.in").unwrap_or_default();
    let parsed = contents.split(',').map(|x| x.parse::<u64>().unwrap_or_default());
    let mut counter = HashMap::from([
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (8, 0)
    ]);
    for value in parsed {
        counter.insert(value, *counter.get(&value).unwrap() + 1);
    }
    for _ in 0..256 {
        let sixth = counter.get(&7).unwrap() + counter.get(&0).unwrap();
        let eighth = counter.get(&0).unwrap() + 0;
        counter.insert(0, *counter.get(&1).unwrap());
        counter.insert(1, *counter.get(&2).unwrap());
        counter.insert(2, *counter.get(&3).unwrap());
        counter.insert(3, *counter.get(&4).unwrap());
        counter.insert(4, *counter.get(&5).unwrap());
        counter.insert(5, *counter.get(&6).unwrap());
        counter.insert(6, sixth);
        counter.insert(7, *counter.get(&8).unwrap());
        counter.insert(8, eighth);
    }
    println!("{}", counter.values().sum::<u64>())
}
