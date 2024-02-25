from setuptools import setup
from xadessri.version import __version__


setup(
    name="xadessri",
    version=__version__,
    url="https://github.com/jsonfm/xades-bes-sri",
    description="A library for signing XML documents using the XADES-BES algorithm, which follows the guidelines of the SRI of Ecuador",
    packages=["xadessri"],
    author="Jason Francisco Macas Mora",
    author_email="franciscomacas3@gmail.com",
    license="AGPL V3",
    install_requires=[
        "cryptography==42.0.5",
        "lxml==5.1.0",
    ],
    extras_require={
        "dev": [
            "lxml-stubs==0.5.1",
            "pytest==8.0.2",
            "setuptools==69.1.1"
        ]
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 (AGPL-3.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
