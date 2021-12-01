#[derive(Clone)]
struct Node {
    label: usize,
    next_label: usize,
}

fn main() {
    let mut cups: Vec<Node> = vec![
        Node {
            label: 0,
            next_label: 0
        };
        1_000_001
    ];
    cups[8] = Node {
        label: 8,
        next_label: 0,
    };
    let mut prev_label = 8;
    for &label in &[5, 3, 1, 9, 2, 6, 4, 7] {
        cups[label] = Node {
            label: label,
            next_label: 0,
        };
        cups[prev_label].next_label = label;
        prev_label = label;
    }
    for label in 10..1_000_001 {
        cups[label] = Node {
            label: label,
            next_label: 0,
        };
        cups[prev_label].next_label = label;
        prev_label = label;
    }
    cups[prev_label].next_label = 8;

    let mut cur_label = cups[8].label;
    for _ in 0..100_000_000 {
        let lift_head_label = cups[cups[cur_label].next_label].label;
        let lift_second_label = cups[cups[lift_head_label].next_label].label;
        let lift_third_label = cups[cups[lift_second_label].next_label].label;
        cups[cur_label].next_label = cups[lift_third_label].next_label;
        let mut dest_label = cur_label;
        loop {
            dest_label -= 1;
            if dest_label == 0 {
                dest_label = 1_000_000;
            }
            if dest_label != lift_head_label
                && dest_label != lift_second_label
                && dest_label != lift_third_label
            {
                break;
            }
        }
        cups[lift_third_label].next_label = cups[dest_label].next_label;
        cups[dest_label].next_label = lift_head_label;
        cur_label = cups[cur_label].next_label;
    }

    println!(
        "{}",
        cups[1].next_label * cups[cups[1].next_label].next_label
    );
}
