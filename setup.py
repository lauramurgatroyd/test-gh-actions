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

import os
from distutils.core import setup
import subprocess

cmd = 'git describe'
dversion = subprocess.check_output(cmd, shell=True).strip().decode('utf-8')[1:]

print ('version {}'.format(dversion))

setup(
      name = "hello-world",
      description = 'Used for testing gh-actions',
	version = dversion,
	packages = {'hello-world', 'hello-world.hello_world'},
      package_dir = {'hello-world': os.path.join('src','hello-world')},
      
)
