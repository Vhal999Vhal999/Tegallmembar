"""Setup configuration for Tegallmembar."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tegallmembar",
    version="0.1.0",
    author="Vhal999Vhal999",
    description="Tegallmembar Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vhal999Vhal999/Tegallmembar",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
