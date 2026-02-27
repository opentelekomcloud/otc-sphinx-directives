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


class third_party_sdk(nodes.General, nodes.Element):
    pass


class ThirdPartySdk(Directive):
    node_class = third_party_sdk
    option_spec = {
        'title': directives.unchanged_required,
        'description': directives.unchanged_required,
        'servicetype': directives.unchanged_required,
    }

    has_content = True

    def run(self):
        node = third_party_sdk()
        node['title'] = self.options.get('title', '')
        node['description'] = self.options.get('description', '')
        node['servicetype'] = self.options.get('servicetype', '').lower().replace(' ', '_')
        
        sdk_list = []
        for line in self.content:
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            if len(parts) >= 4:
                sdk_list.append({
                    'badge': parts[0].strip(),
                    'title': parts[1].strip(),
                    'description': parts[2].strip(),
                    'source_url': parts[3].strip(),
                    'docs_url': parts[4].strip() if len(parts) > 4 else parts[3].strip()
                })
        
        node['sdks'] = sdk_list
        return [node]


def third_party_sdk_html(self, node):
    icon = node['servicetype']
    data = f'''<div class="sdk-service-card">
    <div class="sdk-service-header">
      <div class="sdk-service-title">
        <div class="sdk-service-icon">
          <picture>
            <source class="" srcSet="../../_static/images/services/dark/{icon}.svg" media="(prefers-color-scheme: dark)" />
            <img class="" src="../../_static/images/services/light/{icon}.svg">
          </picture>
        </div>
        <div>
          <h2>{node['title']}</h2>
          <p>{node['description']}</p>
        </div>
      </div>
    </div>

    <div class="sdk-flexbox">
'''

    for sdk in node['sdks']:
        data += f'''
      <div class="sdk-card">
        <div class="sdk-badge">{sdk['badge']}</div>
        <h3>{sdk['title']}</h3>
        <p>{sdk['description']}</p>
        <div class="sdk-actions">
          <scale-button variant="secondary" href="{sdk['source_url']}">View Source</scale-button>
          <scale-button href="{sdk['docs_url']}">Documentation</scale-button>
        </div>
      </div>
'''

    data += '''
    </div>
  </div>
'''
    
    self.body.append(data)
    raise nodes.SkipNode