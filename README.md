# Streamlit Navigation Bar

## Quickstart

Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.

1. Clone this repository:
``` bash
git clone git@github.com:gabrieltempass/streamlit-navigation-bar.git
```

2. Go to the `frontend` directory and initialize and run the component template frontend:
``` bash
cd streamlit-navigation-bar/streamlit_navigation_bar/frontend
```
``` bash
npm install
npm run dev
```

3. From a separate terminal, go to the repository root directory, create a new Python virtual environment, activate it and install Streamlit and the template as an editable package:
``` bash
cd streamlit-navigation-bar
```
``` bash
python3 -m venv venv
. venv/bin/activate
pip install streamlit
pip install -e .
```

Still from the same separate terminal, run the example Streamlit app:
``` bash
streamlit run streamlit_navigation_bar/example.py
```

If all goes well, you should see something like this:

Modify the frontend code at `streamlit_navigation_bar/frontend/src/StNavbar.vue`.
Modify the Python code at `streamlit_navigation_bar/__init__.py`.

## Reference

This Streamlit Component is made from the [streamlit-component-vue-vite-template](https://github.com/gabrieltempass/streamlit-component-vue-vite-template) repository, that uses Vue 3 to code the frontend and Vite to serve the files locally during development, as well as bundle and compile them for production.
