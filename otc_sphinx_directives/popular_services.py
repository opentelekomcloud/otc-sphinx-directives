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

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.util import logging
import json

from otc_metadata.analytics.data import AnalyticsData
import otc_metadata.services

LOG = logging.getLogger(__name__)


class popular_services(nodes.General, nodes.Element):
    pass


class PopularServices(Directive):
    node_class = popular_services

    option_spec = {
        'cloud_environment': directives.unchanged,
    }

    has_content = False

    def run(self):
        node = self.node_class()
        cloud_env = self.options.get('cloud_environment', 'eu_de')
        node['cloud_environment'] = cloud_env
        return [node]

METADATA = otc_metadata.services.Services()

def popular_services_html(self, node):
    # This method renders containers per each service of the category with all
    # links as individual list items

    popular_services = json.dumps(METADATA.all_services_by_cloud_environment(cloud_environment=node['cloud_environment'], environments=['public']))
    data = f'''
        <div class="popular-services">Cloud Environment: {popular_services}</div>
    '''

    self.body.append(data)
    raise nodes.SkipNode


def popular_services_latex(self, node):
    # do nothing
    raise nodes.SkipNode
