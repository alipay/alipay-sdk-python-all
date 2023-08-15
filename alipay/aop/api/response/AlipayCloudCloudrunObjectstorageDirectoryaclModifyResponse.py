#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunObjectstorageDirectoryaclModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageDirectoryaclModifyResponse, self).__init__()
        self._acl = None
        self._file_id = None
        self._file_name = None
        self._last_modified = None

    @property
    def acl(self):
        return self._acl

    @acl.setter
    def acl(self, value):
        self._acl = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self._last_modified = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageDirectoryaclModifyResponse, self).parse_response_content(response_content)
        if 'acl' in response:
            self.acl = response['acl']
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'last_modified' in response:
            self.last_modified = response['last_modified']
