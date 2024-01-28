<template>
  <nav>
    <ul>
      <li v-if="args.logo_svg">
        <a href="#" @click="onClicked(args.logo_page)">
          <span>
            <Logo class="logo"/>
          </span>
        </a>
      </li>
      <li v-for="page in args.pages" :key="page">
        <a href="#" @click="onClicked(page)" :class="{active: page === activePage}">{{ page }}</a>
      </li>
    </ul>
  </nav>
</template>

<script>
import { ref } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"
import Logo from "./logo.svg"

export default {
  name: "StNavbar",
  components: {
    Logo
  },
  props: ["args"], // Arguments that are passed to the plugin in Python are accessible in prop "args"
  setup(props) {
    useStreamlit() // Lifecycle hooks for automatic Streamlit resize

    const activePage = ref(props.args.default)
    const onClicked = (page) => {
      activePage.value = page
      Streamlit.setComponentValue(page)
    }

    return {
      onClicked,
      activePage
    }
  },
}
</script>

<style scoped>
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
nav {
  display: flex;
  background-color: #4285f4;
  height: 45px;
  padding: 0px 30px;
  align-items: center;
}
ul {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
li {
  display: flex;
  align-items: center;
  list-style: none;
}
a {
/*  color: #e3e3e3;*/
  color: white;
  text-decoration: none;
}
.logo {
  display: flex;
  height: 30px;
  width: 30px;
}
.active {
  color: white;
  text-decoration: underline;
  text-underline-offset: 5px;
  text-decoration-thickness: 1.5px;
/*  font-weight: bold;*/
}
</style>
