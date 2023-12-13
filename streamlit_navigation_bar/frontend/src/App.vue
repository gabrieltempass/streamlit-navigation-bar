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
// connection between the component and the Streamlit app, and handles
// passing arguments from Python -> Component.

import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: "App",
  components: {
    StNavbar,
    WithStreamlitConnection
  },
})
</script>

<style>
/*@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');*/
body {
  margin: 0px;
}
#app {
/*  font-family: 'Montserrat', sans-serif;*/
  font-family: 'Source Sans Pro', sans-serif;
/*  font-weight: bold;*/
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
