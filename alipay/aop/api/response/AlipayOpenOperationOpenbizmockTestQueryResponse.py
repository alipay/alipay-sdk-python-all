#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationOpenbizmockTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationOpenbizmockTestQueryResponse, self).__init__()
        self._out_open_id = None
        self._out_test = None

    @property
    def out_open_id(self):
        return self._out_open_id

    @out_open_id.setter
    def out_open_id(self, value):
        self._out_open_id = value
    @property
    def out_test(self):
        return self._out_test

    @out_test.setter
    def out_test(self, value):
        self._out_test = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationOpenbizmockTestQueryResponse, self).parse_response_content(response_content)
        if 'out_open_id' in response:
            self.out_open_id = response['out_open_id']
        if 'out_test' in response:
            self.out_test = response['out_test']
