import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="warpwallet",
    version="1.0",
    author="Arturo Leon",
    author_email="arturo@arturoleon.io",
    description="Implementation of WarpWallet in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arturoleon/warp-wallet-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pycrypto',
        'scrypt',
        'ecdsa',
    ],
)