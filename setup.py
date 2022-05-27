from setuptools import setup, find_packages

setup(
    name="plane",
    version="0.1.0a",
    description="A simple experimental wrapper for the Ravy API",
    url="https://github.com/GoogleGenius/plane",
    author="GoogleGenius",
    author_email="erich.nguyen@outlook.com",
    license="GPLv3",
    packages=find_packages(),
    install_requires=["aiohttp"],
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
