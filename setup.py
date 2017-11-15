from setuptools import setup


setup(
    name='dts-agent',
    packages=['dts_agent'],
    include_package_data=True,
    install_requires=[
        'pyzmq',
        'weewx-orm'
    ]
)
