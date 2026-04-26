from setuptools import setup, find_packages

setup(
    name="promethee-selenium",
    version="1.0.10",
    packages=find_packages(where="lib"),
    package_dir={"": "lib"},
    include_package_data=True,
    install_requires=[
        "selenium-ui-test-tool",
        "pytest",
        "selenium"
    ],
    entry_points={
        "console_scripts": [
            "promethee-selenium=promethee.cli:main",
            "promethee-selenium-docs=promethee.cli:open_docs",
        ],
    },
    author="Yann Dipita",
    description="Promethee-Selenium: A POM-based automated UI test library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    package_data={
        "promethee": ["docs/*"],
    }
)
