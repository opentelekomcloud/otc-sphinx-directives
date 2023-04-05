project = 'otc-sphinx-directives'
copyright = '2023, Ecosystem Squad'
author = 'Open Telekom Cloud Ecosystem Squad'

extensions = [
    'otcdocstheme',
    'otc_sphinx_directives'
]

exclude_patterns = ['_build']
source_suffix = '.rst'
master_doc = 'index'
html_theme = 'otcdocs'
html_static_path = ['_static']