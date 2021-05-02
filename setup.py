import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='deepl.py',
    version='0.0.3',
    author='grarich',
    author_email='grarich123@gmail.com',
    description='A Python wrapper for the DeepL API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/grarich123/deepl.py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
