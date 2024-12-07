use std::fs;

pub fn pt_01(input_path: &str) -> i32 {
    let raw_input = fs::read_to_string(input_path).expect("Should have been able to read the file");
    let parts: Vec<&str> = raw_input.lines().collect();

    let mut result = 0;
    for part in parts {
        let a: Vec<i32> = part
            .split_whitespace()
            .filter_map(|s| s.parse::<i32>().ok())
            .collect();

        let at_least = 1;
        let at_most = 3;
        // either increasing or decreasing filter
        if a.is_sorted_by(|a, b| a < b) || a.is_sorted_by(|a, b| a > b) {
            // counting how many violations of the at_least and at_most filters are done
            let violations_count = a
                .windows(2)
                .filter_map(|pair| {
                    let diff = pair[0] - pair[1];
                    if diff.abs() < at_least || diff.abs() > at_most {
                        Some(diff)
                    } else {
                        None
                    }
                })
                .count() as i32;
            if violations_count == 0 {
                result += 1;
            }
        }
    }
    return result;
}

pub fn pt_02(input_path: &str) -> i32 {
    let mut result = 0;
    return result;
}