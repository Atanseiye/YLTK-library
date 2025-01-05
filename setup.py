from setuptools import setup, find_packages

setup(
    name="my-library",  # Name of your library
    version="0.1.0",  # Version of your library
    packages=find_packages(),  # Automatically find packages in your directory
    install_requires=[],  # List of dependencies, e.g., ['numpy', 'pandas']
    tests_require=["pytest"],  # Test dependencies
    test_suite="tests",  # Directory for tests
    author="Your Name",
    author_email="your.email@example.com",
    description="A description of your library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-library",  # GitHub repository URL
    classifiers=[  # Optional classifiers to help users find your library
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
