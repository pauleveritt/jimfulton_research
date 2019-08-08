from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile('README.rst')
# changes = readfile('CHANGELOG.rst')
changes = ''
requires = [
    'ZODB',
    'waitress',
    'zc.generationalset',
    'transcrypt',
    'pydantic',
]
sample_requires = [
]
testing_requires = [
]

setup(
    name='jimfulton-research',
    version='0.0.1',
    description=(
        'Poke around on some ZODB ideas'
    ),
    long_description=readme + '\n\n' + changes,
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://github.com/pauleveritt/jimfulton_research',
    license='MIT',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=requires,
    extras_require={
        'sample': sample_requires,
        'testing': testing_requires,
    },
    zip_safe=False,
    entry_points={
    },
)
