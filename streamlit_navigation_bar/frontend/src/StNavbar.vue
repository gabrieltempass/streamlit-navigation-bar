<template>
  <nav :style="parseStyles(styles['nav'])">
    <div :style="parseStyles(styles['div'])">
      <ul :style="parseStyles(styles['ul'])">
        <li
          v-if="args.base64_svg"
          :style="parseStyles(styles['li'])"
        >
          <a
            v-if="args.logo_page"
            href="#"
            :style="parseStyles(styles['a'])"
            @click="onClicked(args.logo_page)"
          >
            <img
              :src="`data:image/svg+xml; base64, ${args.base64_svg}`"
              :style="parseStyles(styles['img'])"
            />
          </a>
          <a
            v-else-if="args.logo_page === null"
            :style="parseStyles(styles['a'])"
          >
            <img
              :src="`data:image/svg+xml; base64, ${args.base64_svg}`"
              :style="parseStyles(styles['img'])"
            />
          </a>
        </li>
        <li
          v-for="page in args.pages"
          :key="page"
          :style="parseStyles(styles['li'])"
        >
          <a
            :href="`${args.urls[page][0]}`"
            :target="`${args.urls[page][1]}`"
            :style="parseStyles(styles['a'])"
            @click="onClicked(page)"
          >
            <span
              :data-text="page"
              :class="{selected: page === selectedPage}"
              :style="parseStyles(styles['span']) + parseStyles(styles['selected'], page === selectedPage)"
            >
              {{ page }}
            </span>
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { ref } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"

export default {
  name: "StNavbar",
  // Arguments that are passed to the plugin in Python are accessible in
  // prop "args"
  props: ["args"],

  setup(props) {
    useStreamlit() // Lifecycle hooks for automatic Streamlit resize

    const selectedPage = ref(props.args.default)
    const onClicked = (page) => {
      if (page === props.args.logo_page || props.args.urls[page][0] === "#") {
        selectedPage.value = page
        Streamlit.setComponentValue(page)
      }
    }
    const styles = ref(props.args.styles || {})
    const parseStyles = (dictionary, condition) => {
      if (typeof condition === "undefined") {
        condition = true
      }
      if (!condition) {
        return ""
      }
      let styleString = ""
      for (const key in dictionary) {
        styleString += `${key}:${dictionary[key]};`
      }
      return styleString
    }

    return {
      selectedPage,
      onClicked,
      parseStyles,
      styles
    }
  },
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
nav {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--primary-color);
  font-family: var(--font);
  height: 2.8125rem;
  padding-left: 2rem;
  padding-right: 2rem;
}
div {
  width: 100%;
  max-width: 700px;
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
  text-decoration: none;
}
img {
  display: flex;
  height: 1.875rem;
}
span {
  display: block;
  color: white;
  text-align: center;
}
.selected {
  color: white;
  font-weight: bold;
}
span::before {
  content: attr(data-text);
  display: flex;
  font-weight: bold;
  height: 0;
  overflow: hidden;
  visibility: hidden;
  user-select: none;
  pointer-events: none;
}
</style>
