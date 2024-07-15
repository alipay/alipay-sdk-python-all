#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateFileaddressGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateFileaddressGenerateResponse, self).__init__()
        self._file_url = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateFileaddressGenerateResponse, self).parse_response_content(response_content)
        if 'file_url' in response:
            self.file_url = response['file_url']
