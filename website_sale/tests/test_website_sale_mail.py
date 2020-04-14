# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import eagle
from eagle.tests import tagged
from eagle.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestWebsiteSaleMail(HttpCase):

    def test_01_info_mail_tour(self):
        """The goal of this test is to make sure sending SO by email works."""

        # we override unlink because we don't want the email to be auto deleted
        MailMail = eagle.addons.mail.models.mail_mail.MailMail

        with patch.object(MailMail, 'unlink', lambda self: None):
            self.start_tour("/", 'info_mail', login="admin")
