# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import neuroglancer
import webbrowser as wb


from intern.remote.boss import BossRemote
from intern.resource.boss.resource import ChannelResource

rmt = BossRemote("./boss.cfg")

# Create a resource for the channel you want to access. Let's use a publicly available dataset
collection_name = "my_col"
experiment_name = "my_exp"
channel_name = "my_ch"

channel = ChannelResource(channel_name, collection_name, experiment_name)

x_rng = [0, 2048]
y_rng = [0, 2048]
z_rng = [0, 10]
data = rmt.get_cutout(channel, 0, x_rng, y_rng, z_rng)

# Obtain the bundled Neuroglancer client code (HTML, CSS, and JavaScript) from
# the demo server, so that this example works even if
#
#   python setup.py bundle_client
#
# has not been run.
neuroglancer.set_static_content_source(url='https://neuroglancer-demo.appspot.com')

viewer = neuroglancer.Viewer(voxel_size=[3, 3, 30])
viewer.add(data, name='em')
print(viewer)
print(viewer.get_viewer_url())
wb.open_new_tab(viewer.get_viewer_url())


