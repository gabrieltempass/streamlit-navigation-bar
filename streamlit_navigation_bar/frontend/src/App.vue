<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <StNavbar :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import StNavbar from "./StNavbar.vue"

// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).

import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: "App",
  components: {
    StNavbar,
    WithStreamlitConnection,
  },
})
</script>

<style>
body {
  margin: 0;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
