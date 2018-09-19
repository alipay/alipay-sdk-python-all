#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAuthOrderVoucherCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAuthOrderVoucherCreateResponse, self).__init__()
        self._code_type = None
        self._code_url = None
        self._code_value = None
        self._out_order_no = None
        self._out_request_no = None

    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value
    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAuthOrderVoucherCreateResponse, self).parse_response_content(response_content)
        if 'code_type' in response:
            self.code_type = response['code_type']
        if 'code_url' in response:
            self.code_url = response['code_url']
        if 'code_value' in response:
            self.code_value = response['code_value']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
