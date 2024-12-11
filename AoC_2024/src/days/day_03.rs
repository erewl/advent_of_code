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
    let allowed_clone = allowed.clone();
    let mut allowed_internal = allowed;
    allowed_internal.insert(0, 0); // everything from the start is allowed
    let mut not_allowed_internal = not_allowed;

    if let (Some(last_allowed), Some(last_not_allowed)) = (allowed_internal.last(), not_allowed_internal.last()) {
        if last_allowed > last_not_allowed {
            allowed_internal.push(total_input_length);
        }
        else {
            not_allowed_internal.push(total_input_length);
        }
    }

    println!("{:?}", allowed_internal);
    println!("{:?}", not_allowed_internal);

    let mut ranges: Vec<(i32, i32, bool)> = Vec::new();

    allowed_internal.extend(not_allowed_internal);
    allowed_internal.sort();
    // allowed_internal.push()
    for a in allowed_internal.windows(2) {
        let x: i32 = a[0];
        let y: i32 = a[1];

        if allowed_clone.contains(&x) { // not allowed range
            ranges.push((x, y, true));
        } else {
            ranges.push((x, y, false));
        }
    }
    return ranges;
}

pub fn pt_02(input_path: &str) -> i32 {
    let raw_input = fs::read_to_string(input_path).expect("Should have been able to read the file");
    let multiplicator = Regex::new(r"mul\(\d+,\d+\)").unwrap();

    let allowed = Regex::new(r"do\(\)").unwrap();
    let not_allowed = Regex::new(r"don't\(\)").unwrap();
    let matches = multiplicator.find_iter(&raw_input);
    let allowed_ranges: Vec<i32> = allowed
        .find_iter(&raw_input)
        .map(|a| a.start() as i32)
        .collect();
    let not_allowed_ranges: Vec<i32> = not_allowed
        .find_iter(&raw_input)
        .map(|a| a.start() as i32)
        .collect();

    let mut result: i32 = 0;
    let ranges: Vec<(i32, i32, bool)> = build_ranges(allowed_ranges, not_allowed_ranges, raw_input.len() as i32);
    println!("{:?}", ranges);

    let mut range_index = 0;
    for m in matches {
        // println!("{:?}", m.start());
        let split_instructions: Vec<&str> = m.as_str().split(",").collect();
        let maybe_left = split_instructions[0].split("(").nth(1);
        let maybe_right = split_instructions[1].split(")").nth(0);
        
        let current_range = ranges[range_index];
        let current_position = m.start() as i32;

        println!("{:?} {:?}", current_position, current_range);

        if current_position >= current_range.0 && current_position < current_range.1 {
            if current_range.2 {
                if let (Some(left), Some(right)) = (maybe_left, maybe_right) {
                    if let (Ok(left_int), Ok(right_int)) =
                        (left.trim().parse::<i32>(), right.trim().parse::<i32>())
                    {
                        result += left_int * right_int;
                        // println!("{:?}*{:?}={:?}", left_int, right_int, left_int * right_int)
                    }
                }
            }
        } else {
            range_index += 1;
        }
    }
    return result;
}
