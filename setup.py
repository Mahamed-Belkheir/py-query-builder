import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="query-builder-MahamedBelkheir",
    version="0.0.1",
    author="Mahamed Belkheir",
    author_email="mahamedbelkeir@gmail.com",
    description="a simple sql query builder for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MohamedBelkheirRBK/py-query-builder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)