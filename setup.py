from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='mcmm',
    version='0.0',
    description='',
    long_description=readme(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'],
    url='',
    author='',
    author_email='',
    packages=['mcmm'],
    install_requires=['numpy'],
    tests_require=['nose'],
    test_suite='nose.collector')
