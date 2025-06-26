from setuptools import setup

setup(
    name='rubble',
    version='0.1',
    py_modules=['rubble', 'encode'],
    entry_points={
        'console_scripts': [
            'rubble=rubble:run',
            'rubble-encode=encode:encode_to_rubble',
        ],
    },
)