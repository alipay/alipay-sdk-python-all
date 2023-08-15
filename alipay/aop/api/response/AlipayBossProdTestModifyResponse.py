#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdTestModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdTestModifyResponse, self).__init__()
        self._out_boolean = None
        self._out_date = None
        self._out_number = None
        self._out_number_open_id = None
        self._out_price = None
        self._out_string = None

    @property
    def out_boolean(self):
        return self._out_boolean

    @out_boolean.setter
    def out_boolean(self, value):
        self._out_boolean = value
    @property
    def out_date(self):
        return self._out_date

    @out_date.setter
    def out_date(self, value):
        self._out_date = value
    @property
    def out_number(self):
        return self._out_number

    @out_number.setter
    def out_number(self, value):
        self._out_number = value
    @property
    def out_number_open_id(self):
        return self._out_number_open_id

    @out_number_open_id.setter
    def out_number_open_id(self, value):
        self._out_number_open_id = value
    @property
    def out_price(self):
        return self._out_price

    @out_price.setter
    def out_price(self, value):
        self._out_price = value
    @property
    def out_string(self):
        return self._out_string

    @out_string.setter
    def out_string(self, value):
        self._out_string = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdTestModifyResponse, self).parse_response_content(response_content)
        if 'out_boolean' in response:
            self.out_boolean = response['out_boolean']
        if 'out_date' in response:
            self.out_date = response['out_date']
        if 'out_number' in response:
            self.out_number = response['out_number']
        if 'out_number_open_id' in response:
            self.out_number_open_id = response['out_number_open_id']
        if 'out_price' in response:
            self.out_price = response['out_price']
        if 'out_string' in response:
            self.out_string = response['out_string']
