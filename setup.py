from setuptools import setup, find_namespace_packages
from os import path


# Package metadata.

name = "codeomatic"
description = "A collection of common code for Codeomatic projects."
# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 3 - Alpha"

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as fd:
    readme = fd.read()
with open((path.join(this_directory, 'VERSION'))) as fd:
    version = fd.readline().strip()

# List of dependencies as they appear on PyPI
dependencies = []

setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Denis Nikolskiy",
    author_email="codeomatics@google.com",
    license="Apache 2.0",
    url="https://github.com/codeomatic/core",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=find_namespace_packages(),
    install_requires=dependencies,
    python_requires=">=3.5",
    include_package_data=True,
    zip_safe=False,
)
