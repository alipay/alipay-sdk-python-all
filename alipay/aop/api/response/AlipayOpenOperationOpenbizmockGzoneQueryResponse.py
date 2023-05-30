#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationOpenbizmockGzoneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockGzoneQueryResponse, self).__init__()
        self._result = None
        self._zone_name = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value):
        self._zone_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockGzoneQueryResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
        if 'zone_name' in response:
            self.zone_name = response['zone_name']
