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
              :class="[{active: page === activePage}, hoverColor, hoverBgColor]"
              :style="parseStyles(styles['span']) + parseStyles(styles['active'], page === activePage)"
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

    const activePage = ref(props.args.default)

    const onClicked = (page) => {
      if (page === props.args.logo_page || props.args.urls[page][0] === "#") {
        activePage.value = page
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

    let color = ""
    let bgColor = ""
    if ("hover" in styles.value) {
      const stylesHover = styles.value["hover"]
      if ("color" in stylesHover) {
        color = stylesHover["color"]
      }
      if ("background-color" in stylesHover) {
        bgColor = stylesHover["background-color"]
      }
    }
    let hoverColor = ""
    if (!(color === "")) {
      hoverColor = ref("hover-color")
    }
    let hoverBgColor = ""
    if (!(bgColor === "")) {
      hoverBgColor = ref("hover-bg-color")
    }

    return {
      activePage,
      onClicked,
      styles,
      parseStyles,
      color,
      bgColor,
      hoverColor,
      hoverBgColor,
    }
  },
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

/* HTML tags */
nav {
  align-items: center;
  background-color: var(--secondary-background-color);
  display: flex;
  font-family: var(--font);
  height: 2.875rem;
  justify-content: center;
  padding-left: 2rem;
  padding-right: 2rem;
}
div {
  max-width: 43.75rem;
  width: 100%;
}
ul {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
li {
  align-items: center;
  display: flex;
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
  color: var(--text-color);
  display: block;
  text-align: center;
}

/* Special class that acts as an :active pseudo-class for <span> */
.active {
  color: var(--text-color);
  font-weight: bold;
}

/* Stop the page names from moving when the active <span> is set to bold */
span::before {
  content: attr(data-text);
  display: flex;
  font-weight: bold;
  height: 0;
  overflow: hidden;
  pointer-events: none;
  user-select: none;
  visibility: hidden;
}

/* Both classes with :hover direct the style to <span> */
.hover-color:hover {
  color: v-bind(color) !important;
}
.hover-bg-color:hover {
  background-color: v-bind(bgColor) !important;
}
</style>
