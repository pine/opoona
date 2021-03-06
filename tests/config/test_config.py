# -*- coding: utf-8 -*-

import os
import tempfile
import unittest
from tempfile import NamedTemporaryFile

from mock               import patch
from backports.tempfile import TemporaryDirectory
from six                import StringIO

from opoona.config import Config

class TestConfig(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('opoona.config.Config.get_config_path')
    @patch('opoona.config.Config.get_tmpl_path')
    def test_setup(self, get_tmpl_path, get_config_path, stdout):
        try:
            # create files
            tmpl      = NamedTemporaryFile(delete=False)
            conf_dir  = TemporaryDirectory()
            conf_path = os.path.join(conf_dir.name, '.opoona.yaml')

            tmpl.write('TMPL'.encode('utf-8'))
            tmpl.close()

            # set mock
            get_tmpl_path.return_value   = tmpl.name
            get_config_path.return_value = conf_path

            # check file created
            self.assertFalse(os.path.exists(conf_path))
            Config.setup()
            self.assertTrue(os.path.exists(conf_path))

            # check file content
            with open(conf_path, 'rb') as f:
                self.assertEqual(f.read(), 'TMPL'.encode('utf-8'))

            # check stdout
            message = '`{0}` is created.\n'.format(conf_path)
            self.assertEqual(stdout.getvalue(), message)
        finally:
            os.remove(tmpl.name)
            conf_dir.cleanup()

    @patch('opoona.config.Config.get_config_path')
    def test_init(self, get_config_path):
        get_config_path.return_value = 'HOME/.opoona.yaml'
        config = Config()
        self.assertEqual(config.config_path, 'HOME/.opoona.yaml')
        get_config_path.assert_called()

    def test_load(self):
        try:
            f    = NamedTemporaryFile(delete=False)
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
        finally:
            os.remove(f.name)
