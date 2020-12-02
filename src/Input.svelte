<script lang="ts">
    export let input: String[];
    let text = "Paste input here";
    $: if (text) input = text.split("\n");
</script>

<textarea bind:value={text}/>
<p>Input has {input.length} lines</p>
