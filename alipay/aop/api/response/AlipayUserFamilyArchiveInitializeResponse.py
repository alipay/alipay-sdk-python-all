#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserFamilyArchiveInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFamilyArchiveInitializeResponse, self).__init__()
        self._archive_plugin_url = None

    @property
    def archive_plugin_url(self):
        return self._archive_plugin_url

    @archive_plugin_url.setter
    def archive_plugin_url(self, value):
        self._archive_plugin_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserFamilyArchiveInitializeResponse, self).parse_response_content(response_content)
        if 'archive_plugin_url' in response:
            self.archive_plugin_url = response['archive_plugin_url']
