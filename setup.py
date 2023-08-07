from distutils.util import convert_path

from setuptools import find_packages, setup

# ## Package versioning

# Package version
# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/

# Generic release markers:
# X.Y.0 # For first release after an increment in Y
# X.Y.Z # For bugfix releases

# Admissible pre-release markers:
# X.Y.ZaN # Alpha release
# X.Y.ZbN # Beta release
# X.Y.ZrcN # Release Candidate
# X.Y.Z # Final release

# Dev branch marker is: 'X.Y.dev' or 'X.Y.devN' where N is an integer.
# 'X.Y.dev0' is the canonical version of 'X.Y.dev'

# For instance:
# X increments -> Incompatible w/ previous versions and has foundational changes
# Y incremnts -> Adding functionality, but still backwards compatible
# Z increments -> Backwards compatible and focuses on bug fixes (i.e Defects that are in production)

VERSION = "0.0.1.dev0"

# Install requires
base_packages_path = convert_path("requirements.txt")
with open(base_packages_path) as base_packages_path_file:
    base_packages = base_packages_path_file.read().splitlines()


# Install test-requires
test_packages_path = convert_path("requirements_dev.txt")
with open(test_packages_path) as test_packages_path_file:
    test_packages = test_packages_path_file.read().splitlines()


# METADATA
DISTNAME = "htr"
DESCRIPTION = "short description of project."

with open("docs/README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

MAINTAINER = "Riksarkivet"
LICENSE = "MIT"
PROJECT_URL = "https://Riksarkivet/htr"

def setup_package():
    setup(
        name=DISTNAME,
        maintainer=MAINTAINER,
        description=DESCRIPTION,
        license=LICENSE,
        url=PROJECT_URL,
        version=VERSION,
        long_description=LONG_DESCRIPTION,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows"
        ],
        python_requires=">=3.9",
        install_requires=base_packages,
        include_package_data=True,
        package_dir={"": "src"},
        packages=find_packages(where="src", include=["htr*"]),
        package_data={DISTNAME: ["py.typed"]},
        extras_require={"tests": test_packages},
        data_files=[("requirements", ["requirements.txt", "requirements_dev.txt"])],
    )

if __name__ == "__main__":
    setup_package()
