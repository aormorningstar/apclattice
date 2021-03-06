# apclattice

A final project for APC 524 at Princeton University.

A framework for stochastic dynamics of degrees of freedom on a Bravais lattice. Dynamics are enacted by `Gate` objects acting on the degrees of freedom (`DOF`) of a `Lattice` near a specified location. An implemented example is the honeycomb lattice in two dimensions with a discrete, finite number of particles per site and charge-conserving local dynamics (see demo below).

## Testing

From the top level of the directory (where `test/` is) run

```python
python -m unittest
```

to run all tests.

## Demo

A demo is included at `examples/demo.ipynb`. A bit of profiling is done at the end of the demo.

## Documentation

From within the `docs/` directory run

```shell
make html
make latex
make latexpdf
```

to build the docs in html and pdf format. They are then located at `docs/build/html/index.html` and `docs/build/latex/apclattice.pdf`.

## Report

LaTeX source for the final report is included in `report/`. From that directory run

```shell
pdflatex report.tex
```

to build a pdf of the report.

## Authors

Alan Morningstar and Steven Li as a final project for the APC 524 (Fall 2020) class at Princeton University. Early contributions by Pablo Oyler and Holt Sakai.
