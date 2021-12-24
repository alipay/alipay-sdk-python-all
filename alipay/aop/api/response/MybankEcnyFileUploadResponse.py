#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyFileUploadResponse, self).__init__()
        self._file_id = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyFileUploadResponse, self).parse_response_content(response_content)
        if 'file_id' in response:
            self.file_id = response['file_id']
