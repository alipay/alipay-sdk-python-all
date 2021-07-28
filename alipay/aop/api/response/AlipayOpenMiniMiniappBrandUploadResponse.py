#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniMiniappBrandUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMiniappBrandUploadResponse, self).__init__()
        self._file_key = None

    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMiniappBrandUploadResponse, self).parse_response_content(response_content)
        if 'file_key' in response:
            self.file_key = response['file_key']
