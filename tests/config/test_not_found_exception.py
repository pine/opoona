# -*- coding: utf-8 -*-

import unittest

from opoona.config import NotFoundException

class TestNotFoundException(unittest.TestCase):
    def test_init(self):
        exception = NotFoundException('XXX/config_path')
        self.assertEqual(exception.config_path, 'XXX/config_path')

    def test_str(self):
        exception = NotFoundException('XXX/config_path')
        expect    = "XXX/config_path is required\nTry to exec `opoona setup`"
        self.assertEqual(str(exception), expect)
