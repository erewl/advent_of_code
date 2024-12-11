#[path = "days/day_03.rs"] mod day;

fn main() {

    let day: &str = "03";
    // println!("Test Part 1: {:?}", day::pt_01(&format!("./test/{day}.txt")));
    // println!("Part 1: {:?}", day::pt_01(&format!("./input/{day}.txt")));
    println!("Test Part 2: {:?}", day::pt_02(&format!("./test/{day}.txt")));
    println!("Part 2: {:?}", day::pt_02(&format!("./input/{day}.txt")));
}
