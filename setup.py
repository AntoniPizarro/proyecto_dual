import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Scrapper",
    version="0.0.1",
    author="Toni",
    author2="Pau",
    author_email="apizarro@cifpfbmoll.eu",
    authore_email2="pllinas@cifpfbmoll.eu",
    description="Scrapping Program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntoniPizarro/proyecto_dual.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'certifi==2020.12.5',
        'chardet==3.0.4',
        'idna==2.10',
        'pymongo==3.11.2',
        'requests==2.25.0',
        'urllib3==1.26.3'
    ],
)
