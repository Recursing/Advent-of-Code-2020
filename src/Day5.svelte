<script lang="ts">
    import Input from "./Input.svelte";
    let input = [""];
    let part1 = 0;
    let part2 = 0;
    const mapping = {
        F: 0,
        B: 1,
        R: 1,
        L: 0,
    };
    function parserow(row: String): number {
        const binary = Array.from(row)
            .map((c) => mapping[c])
            .join("");
        return parseInt(binary, 2);
    }
    $: lines = input.map(parserow);
    $: if (lines) {
        part1 = lines.reduce((a, b) => Math.max(a, b));
    }
    $: if (lines) {
        lines.sort((a, b) => a - b);
        for (let index = 0; index < lines.length; index += 1) {
            if (lines[index] + 2 == lines[index + 1]) {
                part2 = lines[index] + 1;
                break;
            }
        }
    }
</script>

<h1>Day 5</h1>
<Input bind:input />
<h2>Part 1: {part1}</h2>
<h2>Part 2: {part2}</h2>
