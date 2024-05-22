from setuptools import setup, find_packages

setup(
    name='erc-sdk',  # The name of your package
    version='0.1',  # The initial release version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'requests',  # External packages as dependencies
    ],
    test_suite='tests',  # Where the tests are located
    url='https://github.com/yourusername/erc-sdk',  # URL of the project
    author='Your Name',  # Your name
    author_email='your.email@example.com',  # Your email
    description='A Python SDK for the ERC APIs',  # A short description of your project
    classifiers=[
        'Programming Language :: Python :: 3',  # The Python version compatibility
        'License :: OSI Approved :: MIT License',  # The license type
        'Operating System :: OS Independent',  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)