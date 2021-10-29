# -*- coding: utf-8 -*-
#   Copyright 2021 Laura Murgatroyd
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


#!/usr/bin/env python3
from distutils.core import setup
import os
import subprocess
    
def version2pep440(version):
    '''normalises the version from git describe to pep440
    
    https://www.python.org/dev/peps/pep-0440/#id29
    '''
    if version[0] == 'v':
        version = version[1:]

    if u'-' in version:
        v = version.split('-')
        v_pep440 = "{}.dev{}".format(v[0], v[1])
    else:
        v_pep440 = version

    return v_pep440


git_version_string = subprocess.check_output('git describe', shell=True).decode("utf-8").rstrip()[1:]
    

#with open("README.rst", "r") as fh:
#    long_description = fh.read()
long_description = 'A number of templates and tools to develop Qt GUIs with Python effectively.'

if os.environ.get('CONDA_BUILD', 0) == '1':
    # if it is a conda build requirements are going to be satisfied by conda
    version = git_version_string
    cwd = os.path.join(os.environ.get('RECIPE_DIR'),'..')
else:
    version = version2pep440(git_version_string)
    cwd = os.getcwd()

    
print ('version {}'.format(version))
print(cwd)
fname = os.path.join(cwd, 'src/hello_world', 'version.py')

if os.path.exists(fname):
    os.remove(fname)
with open(fname, 'w') as f:
    f.write("version = \"{}\"".format(version))

print ('version {}'.format(version))

setup(
      name = "hello-world",
      description = 'Used for testing gh-actions',
	version = version,
	packages = {'hello-world'},
      package_dir = {'hello-world': os.path.join('src','hello-world')},
      
)
