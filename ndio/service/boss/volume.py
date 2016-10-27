﻿# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ndio.service.boss import BossService
from ndio.service.boss.v0_7.volume import VolumeService_0_7

class VolumeService(BossService):
    """VolumeService routes calls to the appropriate API version.
    """
    def __init__(self, base_url, version):
        """Constructor.

        Args:
            base_url (string): Base url (host) of project service such as 'api.boss.io'.
            version (string): Version of Boss API to use.

        Raises:
            (KeyError): if given invalid version.
        """
        BossService.__init__(self)
        self.base_url = base_url
        self._versions = {
            'v0.7': VolumeService_0_7()
        }
        self.service = self.get_api_impl(version)

    def cutout_create(
        self, resource, resolution, x_range, y_range, z_range, numpyVolume, time_range=None):
        """Upload a cutout to the volume service.

        Args:
            resource (ndio.ndresource.resource.Resource): Resource compatible with cutout operations.
            resolution (int): 0 indicates native resolution.
            x_range (list[int]): x range such as [10, 20] which means x>=10 and x<20.
            y_range (list[int]): y range such as [10, 20] which means y>=10 and y<20.
            z_range (list[int]): z range such as [10, 20] which means z>=10 and z<20.
            numpyVolume (numpy.array): A 3D or 4D (time) numpy matrix in (time)ZYX order.
            time_range (optional [list[int]]): time range such as [30, 40] which means t>=30 and t<40.
        """

        return self.service.cutout_create(
            resource, resolution, x_range, y_range, z_range, time_range, numpyVolume,
            self.url_prefix, self.auth, self.session, self.session_send_opts)

    def cutout_get(self, resource, resolution, x_range, y_range, z_range, time_range=None):
        """Get a cutout from the volume service.

        Args:
            resource (ndio.ndresource.boss.resource.ChannelLayerBaseResource): Channel or layer resource.
            resolution (int): 0 indicates native resolution.
            x_range (list[int]): x range such as [10, 20] which means x>=10 and x<20.
            y_range (list[int]): y range such as [10, 20] which means y>=10 and y<20.
            z_range (list[int]): z range such as [10, 20] which means z>=10 and z<20.
            time_range (optional [list[int]]): time range such as [30, 40] which means t>=30 and t<40.

        Returns:
            (numpy.array): A 3D or 4D (time) numpy matrix in (time)ZYX order.

        Raises:
            requests.HTTPError on error.
        """

        return self.service.cutout_get(
            resource, resolution, x_range, y_range, z_range, time_range,
            self.url_prefix, self.auth, self.session, self.session_send_opts)
