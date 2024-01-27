<template>
  <span>
    Hello, {{ args.name }}! &nbsp;
    <button @click="onClicked">Click Me!</button>
  </span>
</template>

<script>
import { ref } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"

export default {
  name: "MyComponent",
  props: ["args"], // Arguments that are passed to the plugin in Python are accessible in prop "args"
  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const numClicks = ref(0)
    const onClicked = () => {
      numClicks.value++
      Streamlit.setComponentValue(numClicks.value)
    }

    return {
      numClicks,
      onClicked,
    }
  },
}
</script>
