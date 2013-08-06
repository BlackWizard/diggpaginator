from distutils.core import setup

setup(
    name='django-diggpaginator',
    version='1.0.0',
    description="Support for Digg-style paginator.",
    long_description=open('README.rst').read(),
    author='Arapov Denis',
    author_email='d.arapov@undev.ru',
    license='BSD',
    url='http://github.com/jordanm/django-hstore',
    packages=[
        'diggpaginator',
    ],
)
