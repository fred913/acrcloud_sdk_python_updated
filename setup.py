import platform
import sys
from os import path

from setuptools import find_packages, setup

package_path = '.'

if sys.platform == "darwin":  # mac
    if platform.machine() == 'arm64':
        package_path = path.join(package_path, "mac", "aarch64")
    else:
        package_path = path.join(package_path, "mac", "x86-64")
elif not sys.platform.startswith('win'):  # linux
    # package_path = path.join(package_path, "linux", "x86-64")
    # check if aarch32 and aarch64
    if platform.machine() == 'aarch64':
        package_path = path.join(package_path, "raspberrypi", "aarch64")
    elif platform.machine() == 'armv7l':
        package_path = path.join(package_path, "raspberrypi", "aarch32")
    else:
        package_path = path.join(package_path, "linux", "x86-64")
elif sys.maxsize > 2**32:  # 64 bit windows
    package_path = path.join(package_path, "windows", "win64")
else:  # 32 bit windows
    package_path = path.join(package_path, "windows", "win32")

if sys.version[0] == '3':
    package_path = path.join(package_path, 'python3')
else:
    package_path = path.join(package_path, 'python2.7')

setup(
    name="pyacrcloud",
    version="1.0.1",
    packages=find_packages(package_path),
    package_dir={"": package_path},
    package_data={
        '': ['*.txt', '*.rst'],
        'acrcloud': ['*.so', '*.pyd'],
    },
    author="ACRCloud",
    author_email="support@acrcloud.com",
    description='Python wrapper for acrcloud libraries',
    license='MIT',
    keywords="ACRCLoud Python SDK",
    url='https://github.com/acrcloud/acrcloud_sdk_python',
    zip_safe=False,
)
