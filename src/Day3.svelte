<script lang="ts">
    import Input from "./Input.svelte";
    let input = [""];
    let part1 = 0;
    let part2 = 0;
    function parserow(row: String): boolean[] {
        return Array.from(row).map((c) => c == "#");
    }
    $: lines = input.map(parserow);
    $: if (lines) {
        part1 = lines.filter((line, index) => line[(index * 3) % line.length])
            .length;
    }
    $: if (lines) {
        const slopes = [
            [1, 1],
            [3, 1],
            [5, 1],
            [7, 1],
            [1, 2],
        ];
        part2 = 1;
        for (let [dx, dy] of slopes) {
            let trees = lines.filter(
                (line, index) =>
                    index % dy == 0 && line[(index * dx/dy) % line.length]
            ).length;
            part2 *= trees;
        }
    }
</script>

<h1>Day 3</h1>
<Input bind:input />
<h2>Part 1: {part1}</h2>
<h2>Part 2: {part2}</h2>
