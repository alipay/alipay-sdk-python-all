#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCityserviceExtOrdercompleteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceExtOrdercompleteQueryResponse, self).__init__()
        self._order_complete_status = None
        self._out_request_no = None
        self._out_trade_no = None

    @property
    def order_complete_status(self):
        return self._order_complete_status

    @order_complete_status.setter
    def order_complete_status(self, value):
        self._order_complete_status = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceExtOrdercompleteQueryResponse, self).parse_response_content(response_content)
        if 'order_complete_status' in response:
            self.order_complete_status = response['order_complete_status']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
