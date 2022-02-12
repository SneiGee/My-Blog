from setuptools import setup

setup(
    name='shareideas',
    version='1.0',
    long_description=__doc__,
    packages=['shareideas'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'flask_sqlalchemy',
        'flask_bcrypt',
        'flask_login',
        'flask_mail',
        'flask_wtf',
        'email_validator',
        'Pillow'
    ]
)
