from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mqtt2gpio",
    version="0.0.1",
    author="Paulo Machado",
    author_email="paulo.mach@gmail.com",
    description="A very crude and direct mqtt to gpio write",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulomach/mqtt2gpio",
    project_urls={
        "Bug Tracker": "https://github.com/paulomach/mqtt2gpio/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: GNU/Linux",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'mqtt2gpio=mqtt2gpio.mqtt2gpio:main'
        ],
    },
    install_requires=[
        'paho-mqtt',
        'gpiozero'
    ]
)
