#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppTestInfo import AppTestInfo


class AlipayOpenAppDanielQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppDanielQueryResponse, self).__init__()
        self._daniel_out_complex = None
        self._daniel_out_price = None
        self._daniel_output = None
        self._output_boolean = None
        self._output_date = None

    @property
    def daniel_out_complex(self):
        return self._daniel_out_complex

    @daniel_out_complex.setter
    def daniel_out_complex(self, value):
        if isinstance(value, AppTestInfo):
            self._daniel_out_complex = value
        else:
            self._daniel_out_complex = AppTestInfo.from_alipay_dict(value)
    @property
    def daniel_out_price(self):
        return self._daniel_out_price

    @daniel_out_price.setter
    def daniel_out_price(self, value):
        self._daniel_out_price = value
    @property
    def daniel_output(self):
        return self._daniel_output

    @daniel_output.setter
    def daniel_output(self, value):
        self._daniel_output = value
    @property
    def output_boolean(self):
        return self._output_boolean

    @output_boolean.setter
    def output_boolean(self, value):
        self._output_boolean = value
    @property
    def output_date(self):
        return self._output_date

    @output_date.setter
    def output_date(self, value):
        self._output_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppDanielQueryResponse, self).parse_response_content(response_content)
        if 'daniel_out_complex' in response:
            self.daniel_out_complex = response['daniel_out_complex']
        if 'daniel_out_price' in response:
            self.daniel_out_price = response['daniel_out_price']
        if 'daniel_output' in response:
            self.daniel_output = response['daniel_output']
        if 'output_boolean' in response:
            self.output_boolean = response['output_boolean']
        if 'output_date' in response:
            self.output_date = response['output_date']
