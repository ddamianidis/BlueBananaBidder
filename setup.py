from setuptools import setup, find_packages
setup(
    name = "bbidder",
    version = "0.0.1",
    packages = find_packages(),
    #scripts = ['bbidder_server', 'bbidder_paserver'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = [
        'docutils>=0.3',
        'connexion>=1.0.31',
        'gevent>=1.1b1',
        'simplejson>=3.11.1',
        'jsonrpcclient>=2.5.1',
        'jsonrpcserver>=3.5.2',
        'jsonschema>=2.6.0',
        'pyzmq>=16.0.2'

    ],
    entry_points = {
        'console_scripts': [
                            'bbidder_server=bbidder.app:main',
                            'bbidder_paserver=bbidder.pa_deamon:main'
                           ],
    },
    
    package_data = {
        'bbidder': ['bidder.conf', 'campaigns_response.json', 'swagger/bluebananabidder.yaml'],
    
    },


    # metadata for upload to PyPI
    author = "Damianos Damianidis",
    author_email = "damidamianidis@gmail.com",
    description = "Blue Banana's Bidder",
    license = "PSF",

    # could also include long_description, download_url, classifiers, etc.
)
