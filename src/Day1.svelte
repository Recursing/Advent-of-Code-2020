<script lang="ts">
    import Input from "./Input.svelte";
    let input = [""];
    let part1 = 0;
    let part2 = 0;
    $: numbers = input.map((s) => parseInt(s, 10));
    $: if (numbers) {
        for (let num1 of numbers) {
            for (let num2 of numbers) {
                if (num1 + num2 == 2020) {
                    part1 = (num1 * num2);
                }
            }
        }
    }
    $: if (numbers) {
        for (let num1 of numbers) {
            for (let num2 of numbers) {
                for (let num3 of numbers){
                    if (num1 + num2 + num3 == 2020) {
                        part2 = (num1 * num2 * num3);
                    }
                }
            }
        }
    }
</script>

<h1>Day 1</h1>
<Input bind:input />
<h2>Part 1: {part1}</h2>
<h2>Part 2: {part2}</h2>