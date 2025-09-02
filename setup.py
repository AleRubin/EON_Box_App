from setuptools import setup

setup(
    name='alarma',
    version='1.0',
    packages=['alarma'],
    package_data={'alarma': ['images/*.png']},  
    install_requires=['PyQt5'],  # Lista todas las dependencias de tu aplicación
    entry_points={
        'console_scripts': [
            'alarma = alarma.main:main',  # Especifica el punto de entrada de tu aplicación
        ]
    },
)