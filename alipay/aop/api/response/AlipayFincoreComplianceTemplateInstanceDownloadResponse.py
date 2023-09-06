#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFincoreComplianceTemplateInstanceDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFincoreComplianceTemplateInstanceDownloadResponse, self).__init__()
        self._down_url = None

    @property
    def down_url(self):
        return self._down_url

    @down_url.setter
    def down_url(self, value):
        self._down_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFincoreComplianceTemplateInstanceDownloadResponse, self).parse_response_content(response_content)
        if 'down_url' in response:
            self.down_url = response['down_url']
