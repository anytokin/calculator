setup(
    name='example',
    version='0.1.0',
    packages=find_packages(include=[ 'calculator.*']),
    install_requires=[
        'numpy >= 1.21.4',
    ]
)