#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

if __name__ == '__main__':
    all_tests = unittest.TestLoader().discover('.')
    result    = unittest.TextTestRunner().run(all_tests).wasSuccessful()
    sys.exit(not result)
