from setuptools import setup, find_packages

setup(
    name='openmuse',
    version='0.1.0',
    author='Mandaliya Vatsal Dharmendrakumar',
    description='A Python-based AI music generator for macOS with Apple M1',
    packages=find_packages(),
    install_requires=[
        'tensorflow==2.4.0',
        'numpy==1.19.5',
        'music21==5.7.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
    ],
)
