#!/usr/bin/env python
from setuptools import find_packages, setup

version = "0.0.7"

setup(
    name="django-turbo-allauth",
    version=version,
    author="Dan Jacob",
    author_email="danjac2018@gmail.com",
    url="https://github.com/hotwire-django/django-turbo-allauth",
    description="Hotwired/Turbo subclasses for allauth views",
    long_description=open("README.md").read() + "\n\n" + open("CHANGES.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.7",
    install_requires=[
        "django (>=3.0)",
        "django-allauth",
        "django-turbo-response (>=0.0.39)",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
