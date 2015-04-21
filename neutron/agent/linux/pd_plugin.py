# Copyright 2015 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc


class PDManagerBase(object):

    def __init__(self, router_id, subnet_id, ri_ifname):
        self.router_id = router_id
        self.subnet_id = subnet_id
        self.ri_ifname = ri_ifname

    @abc.abstractmethod
    def enable(self, pmon, router_ns, ex_gw_ifname, lla):
        pass

    @abc.abstractmethod
    def disable(self, pmon, router_ns):
        pass

    @abc.abstractmethod
    def get_prefix(self):
        pass
