from setuptools import setup

setup(
    name="splatviz_network",
    version="0.0.1",
    description="Network connector for splatviz",
    url="https://github.com/Florian-Barthel/splatviz_network",
    author="Florian Barthel",
    author_email="florian.tim.barthel@hhi.fraunhofer.de",
    license="MIT License",
    packages=["splatviz_network"],
    install_requires=[
        "torch",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python"
    ],
)
