#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdSignatureFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdSignatureFileUploadResponse, self).__init__()
        self._oss_file_id = None

    @property
    def oss_file_id(self):
        return self._oss_file_id

    @oss_file_id.setter
    def oss_file_id(self, value):
        self._oss_file_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdSignatureFileUploadResponse, self).parse_response_content(response_content)
        if 'oss_file_id' in response:
            self.oss_file_id = response['oss_file_id']
