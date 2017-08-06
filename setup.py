DISTNAME = 'fastcat'
DESCRIPTION = 'Navigate English/Japanese Wikipedia categories quickly in a local Redis instance'
AUTHOR = 'Ed Summers'
AUTHOR_EMAIL = 'ehs@pobox.com'
MAINTAINER = 'Takuya Kitazawa'
MAINTAINER_EMAIL = 'k.takuti@gmail.com'
LICENSE = 'CC BY-SA 3.0'
URL = 'https://github.com/takuti/fastcat'


def setup_package():
    from setuptools import setup, find_packages

    metadata = dict(
        name=DISTNAME,
        description=DESCRIPTION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        packages=find_packages(exclude=['*tests*']),
        install_requires=['redis'])

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
