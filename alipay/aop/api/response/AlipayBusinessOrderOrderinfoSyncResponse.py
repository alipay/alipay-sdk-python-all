#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessOrderOrderinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessOrderOrderinfoSyncResponse, self).__init__()
        self._object_id = None
        self._status = None

    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessOrderOrderinfoSyncResponse, self).parse_response_content(response_content)
        if 'object_id' in response:
            self.object_id = response['object_id']
        if 'status' in response:
            self.status = response['status']
