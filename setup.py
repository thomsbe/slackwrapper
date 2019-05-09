import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slackwrapper-thomsbe",
    version="0.0.1",
    author="Thomas Baer",
    author_email="thomas.baer@tbaer.eu",
    description="A small wrapper to easily use the slack client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomsbe/slackwrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)