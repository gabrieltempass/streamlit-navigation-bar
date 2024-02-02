from pathlib import Path

from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="streamlit-navigation-bar",
    version="1.0.0",
    author="Gabriel Tem Pass",
    author_email="redo_hint_0x@icloud.com",
    description="A Streamlit component that allows you to place a navigation bar in your Streamlit app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrieltempass/streamlit-navigation-bar",
    packages=[
        "streamlit_navigation_bar",
    ],
    include_package_data=True,
    package_data={
        "streamlit_navigation_bar": ["adjustments.html"],
    },
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 1.30",
    ],
)
