from pathlib import Path

from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="streamlit-navigation-bar",
    version="3.1.2",
    description="A component that allows you to place a navigation bar in your Streamlit app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrieltempass/streamlit-navigation-bar",
    project_urls={
        "Source Code": "https://github.com/gabrieltempass/streamlit-navigation-bar",
        "Bug Tracker": "https://github.com/gabrieltempass/streamlit-navigation-bar/issues",
        "Release notes": "https://github.com/gabrieltempass/streamlit-navigation-bar/releases",
        "Documentation": "https://github.com/gabrieltempass/streamlit-navigation-bar/wiki",
        "Community": "https://discuss.streamlit.io/t/new-component-streamlit-navigation-bar/66032",
    },
    author="Gabriel Tem Pass",
    author_email="redo_hint_0x@icloud.com",
    license="MIT License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Widget Sets",
    ],
    packages=[
        "streamlit_navigation_bar",
    ],
    include_package_data=True,
    package_data={
        "streamlit_navigation_bar": ["templates/*.css"],
    },
    entry_points={
        "console_scripts": [
            "streamlit-navigation-bar = streamlit_navigation_bar:print_version",
        ]
    },
    python_requires=">=3.8",
    install_requires=[
        "streamlit >= 1.29.0, != 1.32.2",  # Navbar doesn't work with 1.32.2
        "st-theme >= 1.2.2",
    ],
)
