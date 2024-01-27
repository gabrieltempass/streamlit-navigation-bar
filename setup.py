from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-navigation-bar",
    version="0.0.1",
    author="Gabriel Tem Pass",
    author_email="redo_hint_0x@icloud.com",
    description="A Streamlit component that allows you to place a navigation bar in your Streamlit app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrieltempass/streamlit-navigation-bar",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
