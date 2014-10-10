# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack import resource
from openstack.telemetry import telemetry_service


class Meter(resource.Resource):
    id_attribute = 'meter_id'
    resource_key = 'meter'
    base_path = '/v2/meters'
    service = telemetry_service.TelemetryService()

    # Supported Operations
    allow_list = True

    # Properties
    meter_id = resource.prop('meter_id')
    name = resource.prop('name')
    project_id = resource.prop('project_id')
    resource_id = resource.prop('resource_id')
    source = resource.prop('source')
    type = resource.prop('type')
    unit = resource.prop('unit')
    user_id = resource.prop('user_id')
