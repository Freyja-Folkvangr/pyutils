import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyutils',
    version='0.1.4',
    author="freyja-folkvangr",
    author_email="hello@octocat.xyz",
    description="set of util functions for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Freyja-Folkvangr/pyutils",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
 )
