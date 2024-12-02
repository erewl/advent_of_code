use itertools::izip;
use std::fs;

pub fn pt_01(input_path: &str) -> i32 {
    let parts = fs::read_to_string(input_path)
        .expect("Should have been able to read the file");

    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    for part in parts.split("\n") {
        let a: Vec<&str> = part.split_whitespace().collect();
        left.push(a[0].parse::<i32>().expect("Not a valid int"));
        right.push(a[1].parse::<i32>().expect("Not a valid int"));
    }
    left.sort();
    right.sort();


    let mut result = 0;
    for (x, y) in izip!(&left, &right) {
        
        result += (x - y).abs();
    }
    return result
}

pub fn pt_02(input_path: &str) -> i32 {

    let parts = fs::read_to_string(input_path)
        .expect("Should have been able to read the file");

    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    for part in parts.split("\n") {
        let a: Vec<&str> = part.split_whitespace().collect();
        left.push(a[0].parse::<i32>().expect("Not a valid int"));
        right.push(a[1].parse::<i32>().expect("Not a valid int"));
    }

    let mut result = 0;
    for x in left {   
        let occurrences = right.iter().filter(|&n| *n == x).count() as i32;
        result += x * occurrences;
    }
    return result
}