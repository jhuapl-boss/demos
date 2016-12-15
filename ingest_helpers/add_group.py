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

from intern.remote.boss import BossRemote
from intern.resource.boss.resource import *

# Script to create a group and give it read access to a channel

# #### SETUP
grp_name = 'my_team'
collection_name = "my_col"
experiment_name = "my_exp"
coord_frame_name = "my_coord"
channel_name = "my_chan"
# #### SETUP

rmt = BossRemote("./boss.cfg")

print('Creating group . . .')
try:
    rmt.create_group(grp_name)
except Exception as e:
    # Assume group already exists if an exception raised.
    print(e)

# Get the resources
collection = CollectionResource(collection_name)
collection = rmt.get_project(collection)
experiment = ExperimentResource(experiment_name, collection_name, coord_frame_name)
experiment = rmt.get_project(experiment)
channel = ChannelResource(channel_name, collection_name, experiment_name)
channel = rmt.get_project(channel)

# Add perms
perms = ['read']
rmt.add_permissions(grp_name, collection, perms)
rmt.add_permissions(grp_name, experiment, perms)
rmt.add_permissions(grp_name, channel, perms)

