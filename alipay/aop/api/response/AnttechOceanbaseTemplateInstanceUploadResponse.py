#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseTemplateInstanceUploadResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseTemplateInstanceUploadResponse, self).__init__()
        self._biz_id = None
        self._biz_key = None
        self._biz_type = None
        self._expires_at = None
        self._file_key = None
        self._file_type = None
        self._file_url = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_key(self):
        return self._biz_key

    @biz_key.setter
    def biz_key(self, value):
        self._biz_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def expires_at(self):
        return self._expires_at

    @expires_at.setter
    def expires_at(self, value):
        self._expires_at = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseTemplateInstanceUploadResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'biz_key' in response:
            self.biz_key = response['biz_key']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'expires_at' in response:
            self.expires_at = response['expires_at']
        if 'file_key' in response:
            self.file_key = response['file_key']
        if 'file_type' in response:
            self.file_type = response['file_type']
        if 'file_url' in response:
            self.file_url = response['file_url']
