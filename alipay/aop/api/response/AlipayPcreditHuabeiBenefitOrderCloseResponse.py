#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiBenefitOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiBenefitOrderCloseResponse, self).__init__()
        self._order_id = None
        self._out_request_no = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiBenefitOrderCloseResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
