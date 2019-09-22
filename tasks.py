# -*- coding: utf-8 -*-
# Set of scripts for PyPI builds and deploys.
# It assumes the following packages exist:
# invoke, wheel, twine
# For example this works from venv that has those packages.

from invoke import task
from os import path
from invoke.util import cd

project_base = path.abspath(path.dirname(__file__))


def bump(data, version):
    major, minor, fix = [int(chunk.strip()) for chunk in data.strip().split('.')]
    if version == 'major':
        major += 1
    elif version == 'minor':
        minor += 1
    else:
        fix += 1
    return '{}.{}.{}'.format(major, minor, fix)


def update_version_file(version):
    with open(path.join(project_base, 'VERSION'), 'r+') as fd:
        new_version = bump(fd.read(), version)
        fd.seek(0)
        fd.write(new_version)
        fd.truncate()


@task
def build(c):
    """Build and check distribution"""
    with cd(project_base):
        c.run('python setup.py sdist')
        c.run('python setup.py bdist_wheel')
        c.run('twine check dist/*')


@task
def clean(c):
    """Remove previously built distribution"""
    with cd(project_base):
        c.run('rm -rf build dist *.egg-info')


@task
def pypi(c, version, test=False):
    """Upload new major, minor, or fix version to PyPI"""
    clean(c)
    update_version_file(version)
    build(c)
    c.run('twine upload {}dist/*'.format(test and '--repository testpypi ' or ''))
    c.run('git add VERSION')
    c.run('git commit -m "{} version was published to {}."'.format(
        version, test and 'testpypi' or 'pypi')
    )


@task
def test_pypi(c, version):
    pypi(c, version, True)

