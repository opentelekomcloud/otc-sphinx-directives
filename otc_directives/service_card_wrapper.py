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

import yaml

from docutils import nodes

from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.util import logging
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.util.docutils import SphinxDirective, switch_source_input
from docutils.parsers.rst.states import RSTState
from docutils.statemachine import StringList
from docutils.nodes import Element, Node


LOG = logging.getLogger(__name__)

class service_card_wrapper(nodes.General, nodes.Element): 

    def __init__(self, text):
        super(service_card_wrapper, self).__init__()
    
    @staticmethod
    def visit_div(self, node):
        self.body.append(self.starttag(node, 'div class="test"'))
    
    @staticmethod
    def depart_div(self, node=None):
        self.body.append('</div>\n')


class ServiceCardWrapper(SphinxDirective):
    node_class = service_card_wrapper
    option_spec = {
        # 'service_type': directives.unchanged_required,
    }

    has_content = True

    def run(self):

        self.assert_has_content()
        text = '\n'.join(self.content)
        try:
            if self.arguments:
                classes = directives.class_option(self.arguments[0])
            else:
                classes = []
        except ValueError:
            raise self.error(
                'Invalid class attribute value for "%s" directive: "%s".'
                % (self.name, self.arguments[0]))
        node = service_card_wrapper(text)
        node['classes'].extend(classes)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

def setup(app):
    app.add_node(service_card_wrapper, html=(service_card_wrapper.visit_div, service_card_wrapper.depart_div))
    app.add_directive("service_card_wrapper", ServiceCardWrapper)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
