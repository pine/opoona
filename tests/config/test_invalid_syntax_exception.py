# -*- coding: utf-8 -*-

import unittest

from opoona.config import InvalidSyntaxException

class TestInvalidSyntaxException(unittest.TestCase):
    def test_init(self):
        exception = InvalidSyntaxException('XXX/config_path')
        self.assertEqual(exception.config_path, 'XXX/config_path')

    def test_str(self):
        exception = InvalidSyntaxException('XXX/config_path')
        expect    = 'XXX/config_path is invalid syntax'
        self.assertEqual(str(exception), expect)
