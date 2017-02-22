from setuptools import setup

setup(
    name="hwinfoflask",
    packages=["hwinfoflask"],
    include_package_data=True,
    install_requires=[
        "flask",
        "openpyxl",
        "matplotlib",
        ],
    )
