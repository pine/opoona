# -*- coding: utf-8 -*-

import os
import tempfile
import unittest

from mock import patch

from opoona.config import Config

class TestInvalidSyntaxException(unittest.TestCase):
    @patch('os.path.expanduser')
    def test_init(self, expanduser):
        expanduser.return_value = 'HOME/.opoona.yaml'
        config = Config()
        self.assertEqual(config.config_path, 'HOME/.opoona.yaml')
        expanduser.assert_called_with('~/.opoona.yaml')

    def test_load(self):
        f    = tempfile.NamedTemporaryFile(delete=False)
        yaml = '''\
github:
  token: XXX
'''
        f.write(yaml.encode('utf-8'))
        f.close()

        config = Config()
        config.config_path = f.name
        config.load()

        self.assertIsInstance(config['github'], dict)
        self.assertEqual(config['github']['token'], 'XXX')

        os.remove(f.name)
