import setuptools

with open('requirements.txt') as f:
    install_requires = f.read().split('\n')


setuptools.setup(
    name="katazza_bot",
    version="0.0.1",
    author="KatazzaHack",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    # TODO: fill in the rest
    # author_email="author@example.com",
    # description="A small example package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # python_requires='>=3.6',
)
