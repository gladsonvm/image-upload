from setuptools import setup, find_packages

setup(
    name='iman',
    packages=find_packages(),
    url='https://github.abc.com/gladsonvm/fileupload-api',
    description='An api to C/R/U/D files using Django Rest Framework',
    long_description=open('README.md').read(),
    install_requires=[
        "django",
        "djangorestframework",
        ],
    dependency_links = [
     'https://github.com/gladsonvm/image-upload/tarball/master#egg=package-1.0'
    ],
    include_package_data=True,
)