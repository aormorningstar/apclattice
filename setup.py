import setuptools

# take the long description from the README
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apclattice",
    version="0.0.0",
    author="Steven Li, Alan Morningstar, Pablo Oyler, and Holt Sakai",
    description="A package for simulating dynamics of lattice systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
