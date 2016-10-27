from setuptools import setup, find_packages

_PackageName = "cira-labs-leat"
_Namespace = ['cira', 'cira.labs']
_Version = "0.0.2"

_Author = "Canadian Internet Registration Authority"
_Description = "CIRA utility to atomatically renew DANE TLSA records in zone files when a LetsEncrypt certificate is renewed"

ProjectScripts = [
]

PackageData = {
    '': ['*.*'],
}

# Make exe versions of the scripts:
EntryPoints = {
    'console_scripts': [
        'le-at = cira.labs.leat.renew:main'
    ]
}

InstallRequirements = [
    "dnspython", "easyzone3", # DNS tools
]

setup(
    name = _PackageName,
    version = _Version,
    include_package_data=True,
    packages = find_packages('src'),
    package_data = PackageData,
    scripts = ProjectScripts,
    install_requires = InstallRequirements,
    package_dir = {'': 'src'},
    author = _Author,
    description = _Description,
    entry_points = EntryPoints,
    namespace_packages = _Namespace
)