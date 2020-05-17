"""
Utilities to read and process configuration file
"""

import os
import yaml


class ConfigLoader:
    def __init__(self):
        file_path = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..',
            'data',
            'migrations.yml'
        ))

        with open(file_path, 'r') as config_file:
            self.config = yaml.load(config_file, yaml.Loader)

    def get_datasource(self):
        return self.config['datasource']

    def get_migrations_path(self):
        return self.config['migrations_path']