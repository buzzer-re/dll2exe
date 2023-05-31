from setuptools import setup, find_packages

setup(
    name='pe2dll',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'p2dll = pe2dll.main:main'
        ]
    },
    install_requirements=[
        'lief'
    ],
    author='Buzzer',
    description='pe2dll is a Python script that converts PE files to DLLs, allowing custom entry point functions.'
    
)