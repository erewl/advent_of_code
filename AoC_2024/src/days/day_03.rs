use std::fs;

use itertools::{all, izip, Tuples};
use regex::Regex;

pub fn pt_01(input_path: &str) -> i32 {
    let raw_input = fs::read_to_string(input_path).expect("Should have been able to read the file");

    let multiplicator = Regex::new(r"mul\(\d+,\d+\)").unwrap();
    let matches = multiplicator.find_iter(&raw_input);

    let mut result: i32 = 0;
    for m in matches {
        let split_instructions: Vec<&str> = m.as_str().split(",").collect();
        let first = split_instructions[0].split("(").nth(1);
        let second = split_instructions[1].split(")").nth(0);
        if let (Some(f), Some(s)) = (first, second) {
            if let (Ok(parsed_first), Ok(parsed_second)) =
                (f.trim().parse::<i32>(), s.trim().parse::<i32>())
            {
                result += parsed_first * parsed_second;
                // println!("{:?}*{:?}={:?}", parsed_first, parsed_second, parsed_first*parsed_second)
            }
        }
    }
    return result;
}

fn build_ranges(allowed: Vec<i32>, not_allowed: Vec<i32>, total_input_length: i32) -> Vec<(i32, i32, bool)> {
    let internal_not_allowed = allowed.clone();
    let mut allowed_internal = allowed;
    let mut not_allowed_internal = not_allowed;

    let mut ranges: Vec<(i32, i32, bool)> = Vec::new();

    allowed_internal.extend(not_allowed);
    allowed_internal.sort();
    // allowed_internal.push()
    for a in allowed_internal.windows(2) {
        let x: i32 = a[0];
        let y = a[1];

        let mut is_allowed = false;
        if internal_not_allowed.contains(&x) { // not allowed range
            is_allowed = true;
        }
        ranges.push((x, y, is_allowed));
    }
    return ranges;
}

pub fn pt_02(input_path: &str) -> i32 {
    let mut result: i32 = 0;
    return result;
}
