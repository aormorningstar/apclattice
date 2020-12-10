# apclattice

A final project for APC 524 at Princeton University. A framework for stochastic dynamics of degrees of freedom pinned to the sites of a Bravais lattice. Dynamics are enacted by `Gate`s acting on a `Lattice` of degrees of freedom (`DOF`). An implemented example is the honeycomb lattice in two dimensions with a discrete, finite number of particles per site and charge-conserving local dynamics (see demo below).

## Testing

From the top level of the directory (where `test/` is) run

```python
python -m unittest
```

to run all tests.

## Demo

A demo is included at `examples/demo.ipynb`.

## Documentation

From within the `docs/` directory run

```shell
make html
```

to build the docs in html format. They are then located at `docs/build/html/index.html`.

## TODO
* more tests
* get LaTeX docs to work
* write report

## Authors

Alan Morningstar and Steven Li as a final project for the APC 524 (Fall 2020) class at Princeton University. Early contributions by Pablo Oyler and Holt Sakai.
