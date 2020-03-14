import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlpsummary-sam_ubcmds", # Replace with your own username
    version="1.0.0",
    author="UBC MDS Team 21",
    author_email="",
    description="A useful tool for summarizing NLP data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UBC-MDS/nlpsummarize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
