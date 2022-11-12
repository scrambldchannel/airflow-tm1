#!/usr/bin/env python
# coding: utf8

from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="airflow-provider-tm1",
    packages=["src/tm1_provider", *(f"tm1_provider.{package}" for package in find_packages("/src/tm1_provider"))],
    version="0.0.8",
    description="A TM1 provider for Apache Airflow",
    long_description=readme,
    long_description_content_type="text/markdown",
    entry_points={
        "apache_airflow_provider": [
            "provider_info=tm1_provider.__init__:get_provider_info",
        ],
    },
    license="Apache License 2.0",
    author="Alexander Sutcliffe",
    author_email="sutcliffe.alex@gmail.com",
    python_requires=">=3.7.0",
    install_requires=[
        "apache-airflow~=2.2.0",
        # is there any need to support that far back?
        "tm1py~=1.1",
    ],
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/scrambldchannel/airflow-provider-tm1",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Apache Airflow",
        "Framework :: Apache Airflow :: Provider",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
)
