#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenFileUploadResponse, self).__init__()
        self._extern_id = None
        self._file_id = None

    @property
    def extern_id(self):
        return self._extern_id

    @extern_id.setter
    def extern_id(self, value):
        self._extern_id = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenFileUploadResponse, self).parse_response_content(response_content)
        if 'extern_id' in response:
            self.extern_id = response['extern_id']
        if 'file_id' in response:
            self.file_id = response['file_id']
