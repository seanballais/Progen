from distutils.core import setup
from progen.version import __version__

setup(
    name="Progen",
    version=__version__,
    author="Sean Francis N. Ballais",
    author_email="sfballais123@gmail.com",
    packages=["progen"],
    include_package_data=True,
    url="https://www.github.com/seanballais/Progen",
    license="LICENSE",
    description="Generate projects",
    long_description=open("README.md").read(),
)

