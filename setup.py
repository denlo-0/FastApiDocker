from setuptools import setup

setup(
    name = 'app',
    version =  '0.0',
    author = 'Vvvv',
    descriptioin = 'FastApi app',
    install_requires = [
        "fastapi==0.70.0",
        "uvicorn==0.15.0",
        "requests==2.26.0",
    ],
    scripts = ['app/main.py'],
)