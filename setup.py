import os
from setuptools import setup

setup(
    name='avocado',
    version='0.1',
    description='Photometric Classification of Astronomical Transients and '
    'Variables With Biased Spectroscopic Samples',
    url='http://github.com/kboone/avocado',
    author='Kyle Boone',
    author_email='kboone@berkeley.edu',
    license='BSD',
    packages=['avocado'],
    data_files=[('', ['avocado_settings.json'])],
    exclude_package_data = {'': ['.gitignore', 'scripts/data/*']},
    scripts=['scripts/' + f for f in os.listdir('scripts') if os.path.isfile(os.path.join('scripts', f))],
)
