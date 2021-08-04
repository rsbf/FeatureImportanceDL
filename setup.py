from setuptools import setup, find_packages

setup(
    name="fir_dl",
    version="1.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6"
)


