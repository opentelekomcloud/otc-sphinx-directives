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


LOG = logging.getLogger(__name__)


# def sort_docs(docs):
#     umn = ''
#     api_ref = ''
#     i = 0
#     for doc in docs:
#         if doc['type'] == 'umn':
#             umn = doc
#             docs.pop(i)
#         elif doc['type'] == 'api-ref':
#             api_ref = doc
#             docs.pop(i)
#         i += 1

#     sorted_docs = docs
#     if umn:
#         sorted_docs.insert(0, umn)
#     if api_ref:
#         sorted_docs.insert(1, api_ref)
#     return sorted_docs


class article_author(nodes.General, nodes.Element):
    pass


METADATA = otc_metadata.services.Services()


class ArticleAuthor(Directive):
    node_class = article_author
    option_spec = {
        'author': directives.unchanged_required,
        'date': directives.unchanged_required,
        'link': directives.unchanged,
        'picture': directives.unchanged,
        'picture_alt': directives.unchanged,
        'city': directives.unchanged,
    }

    has_content = False

    def run(self):
        node = self.node_class()
        # for k in self.option_spec:
        #     if self.options.get(k):
        #         node[k] = self.options.get(k)
        #     elif k == 'environment':
        #         node[k] = 'public'
        #     else:
        #         node[k] = ''

        return [node]


def article_html(self, node):
    # article_authors are used to reprent people who wrote an Architecture Center blog or article entry

    data = ''

    data += (
        f'''
            <div>
                <img alt="{node["picture_alt"]}" src="{node["picture"]}"></img>
                <div>
                    <div>{node["author"]}</div>
                    <div>{node["city"]}, {node["date"]}</div>            
                </div>
            </div>
        ''')

    self.body.append(data)
    raise nodes.SkipNode


def service_card_latex(self, node):
    # do nothing
    raise nodes.SkipNode
