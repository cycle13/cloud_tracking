from distutils.core import setup

setup(
    name='cloud_tracking',
    version='0.1.3',
    packages=['cloud_tracking'],
    url='https://github.com/markmuetz/cloud_tracking',
    license='',
    author='markmuetz',
    author_email='mark.muetzelfeldt@reading.ac.uk',
    description='Simple cloud tracking',
    requires=['numpy', 'iris', 'matplotlib'],
    scripts=['bin/track_clouds'],
)
