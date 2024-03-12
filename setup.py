from pathlib import Path

from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="streamlit-navigation-bar",
    version="2.0.1",
    author="Gabriel Tem Pass",
    author_email="redo_hint_0x@icloud.com",
    description="A component that allows you to place a navigation bar in your Streamlit app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrieltempass/streamlit-navigation-bar",
    packages=[
        "streamlit_navigation_bar",
    ],
    include_package_data=True,
    package_data={
        "streamlit_navigation_bar": ["templates/*.css"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit >= 1.30",
        "st-theme >= 1.1.0",
    ],
)
