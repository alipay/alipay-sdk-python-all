#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationTestOpenapiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationTestOpenapiQueryResponse, self).__init__()
        self._out_open_id = None
        self._out_type = None
        self._out_uid = None

    @property
    def out_open_id(self):
        return self._out_open_id

    @out_open_id.setter
    def out_open_id(self, value):
        self._out_open_id = value
    @property
    def out_type(self):
        return self._out_type

    @out_type.setter
    def out_type(self, value):
        self._out_type = value
    @property
    def out_uid(self):
        return self._out_uid

    @out_uid.setter
    def out_uid(self, value):
        self._out_uid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationTestOpenapiQueryResponse, self).parse_response_content(response_content)
        if 'out_open_id' in response:
            self.out_open_id = response['out_open_id']
        if 'out_type' in response:
            self.out_type = response['out_type']
        if 'out_uid' in response:
            self.out_uid = response['out_uid']
