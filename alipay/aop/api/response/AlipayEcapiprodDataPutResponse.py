#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcapiprodDataPutResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDataPutResponse, self).__init__()
        self._data_version = None

    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDataPutResponse, self).parse_response_content(response_content)
        if 'data_version' in response:
            self.data_version = response['data_version']
