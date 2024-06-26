# ODESOLVE

### Odesolve is a library that implements various methods for solving ordinary differential equations in Python.  Analytic, semi-analytic, numerical, and machine learning methods are to be implemented in an easy-to-use package.  The goal is to provide a comprehensive library for solving ODEs in Python.

Dependencies:
See `requirements.txt` for dependencies.


## Development

Install development dependencies with `pip install -r requirements-dev.txt`.

Install package dependencies with `pip install -r requirements.txt`.

Setup pre-commit:

```bash
pre-commit install
```

Run pre-commit checks after `git add` but before `git commit`

```bash
pre-commit run --all-files
```

Install the package in development mode:

```bash
pip install -e .
```

Run tests:

```bash
pytest
```

Run linter:

```bash
black .
```

Run type checker:

```bash
mypy ode_solve
```

Run import sorter:

```bash
isort .
```
