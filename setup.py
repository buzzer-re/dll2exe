from setuptools import setup, find_packages

setup(
    name='dll2exe',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dll2exe = dll2exe.dll2exe:main'
        ]
    },
    install_requirements=[
        'lief'
    ],
    author='Buzzer',
    long_description='dll2exe is a Python script that converts PE files to DLLs, allowing custom entry point functions.'
    
)