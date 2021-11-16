#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingPayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingPayApplyResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._parking_order_no = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def parking_order_no(self):
        return self._parking_order_no

    @parking_order_no.setter
    def parking_order_no(self, value):
        self._parking_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingPayApplyResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'parking_order_no' in response:
            self.parking_order_no = response['parking_order_no']
