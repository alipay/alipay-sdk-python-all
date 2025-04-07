#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePropertyFileUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePropertyFileUploadResponse, self).__init__()
        self._biz_id = None
        self._file_key = None
        self._file_name = None
        self._file_url = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePropertyFileUploadResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'file_key' in response:
            self.file_key = response['file_key']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'file_url' in response:
            self.file_url = response['file_url']
