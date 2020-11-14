import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stochasticlattice-aormorningstar",
    version="0.0.0",
    author="Steven Li, Alan Morningstar, Pablo Oyler, and Holt Sakai",
    author_email="aormorningstar@gmail.com",
    description="A package for simulating stochastic dynamics of lattice systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holt-sakai/APC_Lattice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)