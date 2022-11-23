#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDataSssCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataSssCreateResponse, self).__init__()
        self._c = None
        self._c_open_id = None

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def c_open_id(self):
        return self._c_open_id

    @c_open_id.setter
    def c_open_id(self, value):
        self._c_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataSssCreateResponse, self).parse_response_content(response_content)
        if 'c' in response:
            self.c = response['c']
        if 'c_open_id' in response:
            self.c_open_id = response['c_open_id']
