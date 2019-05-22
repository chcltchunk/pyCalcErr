from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='pyCalcErr',
     version='0.4',
     author="Jonas Oldenstaedt",
     description="Gauss error propagation with latex formula",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/chcltchunk/pyCalcErr",
     packages=['pyCalcErr'],
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=["pytexit", "sympy"],
     python_requires='>=3',
     entry_points={
        "console_scripts": [
            "pyCalcErr=pyCalcErr.pyCalcErr:main",
        ]
    },
 )
