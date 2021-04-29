import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devmail",
    version="0.0.3",
    author="Faruq Sandi",
    author_email="<faruqsandi@email.com>",
    description="DeveloperMail Python Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/faruqsandi/devmail",
    project_urls={
        "Bug Tracker": "https://github.com/faruqsandi/devmail/issues",
    },
    keywords=['python', 'developermail', 'temp mail', 'developer mail'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['requests']
)
