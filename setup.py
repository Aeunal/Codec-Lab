from setuptools import setup, find_packages

setup(
    name='CodecLab',
    version='0.1.0',  # TODO Update the version number for new releases
    author='Ahmet Emin Ünal',
    author_email='aeunal@hotmail.com',
    description='A flexible framework for implementing and testing codecs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Aeunal/Codec-Lab',  # Replace with your repository URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your project dependencies here,
        # e.g., 'numpy', 'scipy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Change as appropriate
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: MIT License',  # Change the license if different
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Adjust minimum version as needed
    entry_points={
        'console_scripts': [
            # If you have any scripts that should be installed, list them here
            # e.g., 'codeclab-cli=codeclab.cli:main',
        ],
    },
)
