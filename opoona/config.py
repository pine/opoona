# -*- coding: utf-8 -*-

import os

import yaml


class FileAlreadyExistsException(Exception):
    def __init__(self, config_path):
        self.config_path = config_path

    def __str__(self):
        return '`{0}` is already exists.'.format(self.config_path)


class NotFoundException(Exception):
    def __init__(self, config_path):
        self.config_path = config_path

    def __str__(self):
        return "\n".join([
            '`{0}` is required'.format(self.config_path),
            'try to exec `opoona setup`',
        ])


class InvalidSyntaxException(Exception):
    def __init__(self, config_path):
        self.config_path = config_path

    def __str__(self):
        return '{0} is invalid syntax'.format(self.config_path)


class Config(dict):
    @classmethod
    def get_config_path(cls):
        return os.path.expanduser('~/.opoona.yaml')

    @classmethod
    def get_tmpl_path(cls):
        return os.path.join(os.path.dirname(__file__), 'config_tmpl.yaml')

    @classmethod
    def setup(cls):
        config_path = cls.get_config_path()
        if os.path.exists(config_path):
            raise FileAlreadyExistsException(config_path)

        with open(cls.get_tmpl_path(), 'r') as tmpl:
            with open(config_path, 'w') as conf:
                conf.write(tmpl.read())

        print('`{0}` is created.'.format(config_path))

    def __init__(self):
        self.config_path = Config.get_config_path()

    def load(self):
        if not os.path.exists(self.config_path):
            raise NotFoundException(self.config_path)

        with open(self.config_path) as f:
            config = yaml.load(f)
            if not isinstance(config, dict):
                raise InvalidSyntaxException(self.config_path)
            self.update(config)
