# -*- coding: utf-8 -*-

# Import python libs
from __future__ import absolute_import, print_function, unicode_literals

import salt.config
import salt.loader

# Import Salt Testing libs
from tests.support.unit import TestCase


class ConfirmTop(TestCase):
    def setUp(self):
        opts = salt.config.DEFAULT_MINION_OPTS.copy()
        self.matchers = salt.loader.matchers(opts)

    def test_sanity(self):
        match = self.matchers["confirm_top.confirm_top"]
        self.assertTrue(match("*", []))
