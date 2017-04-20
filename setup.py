from distutils.core import setup

setup(
    name='pptholer',
    version='0.0.1',
    install_requires=['Click', 'python-pptx'],
    packages=['pptholer'],
    url='',
    license='MIT',
    author='rino0601.dev@gmail.com',
    author_email='rino0601.dev@gmail.com',
    description='',
    entry_points={
        'console_scripts': [
            'pptholer = pptholer.main:cli',
        ], },
    zip_safe=False,
)
