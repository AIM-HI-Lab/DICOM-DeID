from setuptools import setup, find_packages

setup(
    name='dicom_deid',
    version='0.0.0',  # Your package's initial version
    description=(
        'A library to deidentify DICOM images for transfer.'
    ),
    packages=find_packages(),
    install_requires=[
        # Requirements.txt file
    ],
    classifiers=[
        # 'Programming Language :: Python :: 3.10',
        # Add more classifiers as needed
    ],
    python_requires='>=3.8',  # Minimum version requirement of the package
)
