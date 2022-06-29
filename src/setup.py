"""Setup files for the seis package."""

from setuptools import setup

setup(
    name="seis",
    version="0.0.1",
    description="SEIS model for epidemic disease",
    maintainer="Shumeng Lin",
    maintainer_email="lsm19971229@gmail.com",
    license="GPL",
    packages=["seis"],
    scripts=["seis/seis.py"],
    setup_requires=[],
    data_files=["LICENSE"],
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
    ],
    long_description="""\
    The package to quickly solve and analyze SEIS model.
    Results can be plots or .dat file.
      """,
)
