<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <MyComponent :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import MyComponent from "./MyComponent.vue"

// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).

import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: "App",
  components: {
    MyComponent,
    WithStreamlitConnection,
  },
})
</script>

<style>
body {
  margin: 0px;
}
#app {
  color: var(--text-color);
  font-family: var(--font);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
