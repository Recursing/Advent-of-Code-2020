<script lang="ts">
    import Input from "./Input.svelte";
    let input = [""];
    let part1 = 0;
    let part2 = 0;
    const pattern = /(\d+)-(\d+) ([a-z]): ([a-z]+)/;
    function parserow(row: String): [number, number, string, string] {
        let groups = row.match(pattern);
        if (!groups || groups.length != 5) return [0, 0, "", ""];
        const [all, mins, maxs, letter, string] = groups;
        const min = parseInt(mins, 10);
        const max = parseInt(maxs, 10);
        return [min, max, letter, string];
    }
    $: lines = input.map(parserow).filter((l) => l[0]);
    $: if (lines) {
        part1 = lines.filter(([min, max, letter, string]) => {
            const occ = string.split(letter).length - 1;
            return occ >= min && occ <= max;
        }).length;
    }
    $: if (lines) {
        part2 = lines.filter(([min, max, letter, string]) => {
            return (string[min - 1] == letter) != (string[max - 1] == letter);
        }).length;
    }
</script>

<h1>Day 2</h1>
<Input bind:input />
<h2>Part 1: {part1}</h2>
<h2>Part 2: {part2}</h2>
