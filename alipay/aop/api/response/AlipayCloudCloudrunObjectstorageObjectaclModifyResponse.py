#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunObjectstorageObjectaclModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstorageObjectaclModifyResponse, self).__init__()
        self._acl = None
        self._file_id = None
        self._file_name = None
        self._size = None
        self._status = None

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
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstorageObjectaclModifyResponse, self).parse_response_content(response_content)
        if 'acl' in response:
            self.acl = response['acl']
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'size' in response:
            self.size = response['size']
        if 'status' in response:
            self.status = response['status']
