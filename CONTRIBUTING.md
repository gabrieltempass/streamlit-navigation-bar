# Contributing

Thanks for your interest in helping improve the Streamlit Navigation Bar! This
guide is for people who want to contribute code to the project. There are other
ways to contribute, such as [reporting a bug](https://github.com/gabrieltempass/streamlit-navigation-bar/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml)
or [requesting a feature](https://github.com/gabrieltempass/streamlit-navigation-bar/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml).
You can also just [ask a question](https://github.com/gabrieltempass/streamlit-navigation-bar/issues/new?assignees=&labels=question&projects=&template=ask_question.yml),
if you want. Note that we have a [code of conduct](https://github.com/gabrieltempass/streamlit-navigation-bar/blob/main/CODE_OF_CONDUCT.md),
please follow it in all your interactions with the project.

## Before starting

If your contribution is more than a few lines of code, then prior to starting
to code on it please post in the respective issue saying you want to volunteer,
and then wait for a positive response. If there is no issue for it yet, create
it first. This helps make sure:

* Two people aren't working on the same thing
* This is something the project's maintainers believe should be implemented or
  fixed
* Any API, UI, or deeper architectural changes that need to be implemented have
  been fully thought through by the project's maintainers
* Your time is well spent!

## Style guide

We use [Black](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARsAnNdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIm75UxzLdMMp-XXRCzahizn0Ex32wRFDOpjVE9rszhHWIRPMyyAAArN1JGAnzo0EAAY8F7QgAAP01Vc6xxGf7AgAAAAAEWVo=),
with a line length of 80, to format the code. Besides that, [Streamlit's
oficial style guide](https://github.com/streamlit/streamlit/wiki/Style-Guide) is followed
throughout the project. 

## Development

Ensure you have [Python 3.8+](https://www.python.org/downloads/),
[Node.js](https://nodejs.org) and
[npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
installed.

1. Fork [the repository](https://github.com/gabrieltempass/streamlit-navigation-bar)
via the user interface on GitHub and then do the following:

``` bash
git clone https://github.com/${YOUR_NAME}/streamlit-navigation-bar.git
```

``` bash
cd streamlit-navigation-bar
```

``` bash
git remote add remote https://github.com/gabrieltempass/streamlit-navigation-bar.git
git checkout develop
git submodule update --init
git checkout -b ${BRANCH_NAME}
```

2. Go to the `frontend` directory and initialize and run the component frontend:
``` bash
cd streamlit_navigation_bar/frontend
```
``` bash
npm install
npm run dev
```

3. From a separate terminal, go to the repository root directory, create a new
Python virtual environment, activate it and install Streamlit,
[st-theme](https://github.com/gabrieltempass/streamlit-theme) and the directory
as an editable package:
``` bash
cd streamlit-navigation-bar
```
``` bash
python3 -m venv venv
. venv/bin/activate
pip install streamlit
pip install st-theme
pip install -e .
```

Still from the same separate terminal, run the example Streamlit app:
``` bash
streamlit run streamlit_navigation_bar/example.py
```

If all goes well, you should see something like this:

![Quickstart success](https://github.com/gabrieltempass/streamlit-navigation-bar/raw/main/images/development.png)

Modify the frontend code at
`streamlit_navigation_bar/frontend/src/StNavbar.vue`.
Modify the Python code at `streamlit_navigation_bar/__init__.py`.

4. Submit your pull request.
