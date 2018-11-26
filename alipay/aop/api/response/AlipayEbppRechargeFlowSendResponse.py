#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppRechargeFlowSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppRechargeFlowSendResponse, self).__init__()
        self._ext_msg = None
        self._merchant_order_id = None
        self._status = None
        self._trade_id = None

    @property
    def ext_msg(self):
        return self._ext_msg

    @ext_msg.setter
    def ext_msg(self, value):
        self._ext_msg = value
    @property
    def merchant_order_id(self):
        return self._merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self._merchant_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppRechargeFlowSendResponse, self).parse_response_content(response_content)
        if 'ext_msg' in response:
            self.ext_msg = response['ext_msg']
        if 'merchant_order_id' in response:
            self.merchant_order_id = response['merchant_order_id']
        if 'status' in response:
            self.status = response['status']
        if 'trade_id' in response:
            self.trade_id = response['trade_id']
