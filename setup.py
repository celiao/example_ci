import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_ci",
    version="0.0.1",
    author="Celia Oakley",
    author_email="celia.oakley@alumni.stanford.edu",
    description="A small example package utilizing GitHub Actions, specifically continuous integraiton(CI)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/celiao/example_ci",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
