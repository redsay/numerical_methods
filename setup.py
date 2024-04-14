import os

from setuptools import setup


def _read_requirements():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
        return f.read().splitlines()


setup(
    name="ode_solve",
    packages=["ode_solve"],
    version="0.1",
    install_requires=_read_requirements(),
    description="""A package implementing analytic, semi-analytic,
    numerical and machine learning methods for solving ordinary differential equations""",
)
