# -*- coding: utf-8 -*-

import os

import yaml


class NotFoundException(Exception):
    def __init__(self, config_path):
        self.config_path = config_path

    def __str__(self):
        return "\n".join([
            '{0} is required'.format(self.config_path),
            'try to exec `opoona setup`',
        ])


class InvalidSyntaxException(Exception):
    def __init__(self, config_path):
        self.config_path = config_path

    def __str__(self):
        return '{0} is invalid syntax'.format(self.config_path)


class Config(dict):
    @classmethod
    def setup(cls):
        pass

    def __init__(self):
        self.config_path = os.path.expanduser('~/.opoona.yaml')

    def load(self):
        if not os.path.exists(self.config_path):
            raise NotFoundException(self.config_path)

        with open(self.config_path) as f:
            config = yaml.load(f)
            if not isinstance(config, dict):
                raise InvalidSyntaxException(self.config_path)
            self.update(config)
