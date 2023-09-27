#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudrunObjectstoragePermissionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunObjectstoragePermissionQueryResponse, self).__init__()
        self._read_permission = None

    @property
    def read_permission(self):
        return self._read_permission

    @read_permission.setter
    def read_permission(self, value):
        self._read_permission = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunObjectstoragePermissionQueryResponse, self).parse_response_content(response_content)
        if 'read_permission' in response:
            self.read_permission = response['read_permission']
