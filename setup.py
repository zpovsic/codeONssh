from setuptools import setup
from setuptools import find_packages

with open("README.md") as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(
        name="codeONssh",
        scripts=["scripts/codeONssh"],
        version="0.0.1",
        description="codeONssh - Run code on Colab or Kaggle",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="pz",
        author_email="povsic.zdravko@gmail.com",
        url="https://github.com/zpovsic/codeONssh",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=["pyngrok>=4.1.11"],
        platforms=["linux", "unix", "windows"],
        python_requires=">3.5.2",
    )
