#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoFileUploadResponse, self).__init__()
        self._file_id = None
        self._safed = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def safed(self):
        return self._safed

    @safed.setter
    def safed(self, value):
        self._safed = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoFileUploadResponse, self).parse_response_content(response_content)
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'safed' in response:
            self.safed = response['safed']
