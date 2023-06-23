"""
--------------------------------------
Build documentation
---------------------------------------
pip3.9 install tqdm
pip3.9 install setuptools
pip3.9 install wheel
pip3.9 install bdist_wheel

python3.9 setup.py bdist_wheel
"""


import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='python-camelcaser',
    version='0.1.0b',
    packages=setuptools.find_packages(),
    package_data={'camelcaser': ['*.txt', 'word_lists/*.txt']},
    include_package_data=True,
    author="Benjamin Schaedlich",
    description="Convert strings to camel, snake and kebab case - even if separation is unknown.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benschaedlich/python-camelcaser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyenchant==3.2.2',
    ],
    project_urls={
        "Documentation": "https://github.com/benschaedlich/python-camelcaser",
        "Source": "https://github.com/benschaedlich/python-camelcaser",
    },
)
