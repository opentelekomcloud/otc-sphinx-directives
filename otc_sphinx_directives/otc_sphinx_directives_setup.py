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

from otc_sphinx_directives.directive_wrapper import directive_wrapper, DirectiveWrapper
from otc_sphinx_directives.service_card import service_card, service_card_html, ServiceCard


def latex_do_nothing(self, node):
    # do nothing
    raise nodes.SkipNode

def setup(app):
    app.add_node(
        directive_wrapper,
        html=(directive_wrapper.visit_div, directive_wrapper.depart_div),
        latex=(latex_do_nothing))
    app.add_directive("directive_wrapper", DirectiveWrapper)
    app.add_node(
        service_card,
        html=(service_card_html, None),
        latex=(latex_do_nothing, None))
    app.add_directive("service_card", ServiceCard)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
