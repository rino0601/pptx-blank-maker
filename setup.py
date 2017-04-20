from setuptools import setup

setup(
    name='pptxblank',
    version='0.0.1',
    install_requires=['Click', 'python-pptx'],
    packages=['pptxblank'],
    url='',
    license='MIT',
    author='rino0601.dev@gmail.com',
    author_email='rino0601.dev@gmail.com',
    description='',
    entry_points='''
        [console_scripts]
        pptxblank=pptxblank.main:cli
    ''',
)
