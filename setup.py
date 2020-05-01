import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pythonw",
    version="3.0.3",
    author="ali sayfi",
    author_email="ali.35351@gmail.com.com",
    url="http://yobinet.ir",
    description="python instructions example",
    packages=setuptools.find_packages(),
    long_description='long description',
    long_description_content_type='text/x-rst',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)