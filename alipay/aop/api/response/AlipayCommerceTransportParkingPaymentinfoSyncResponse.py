#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportParkingPaymentinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportParkingPaymentinfoSyncResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._send_parking_message_flag = None

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
    def send_parking_message_flag(self):
        return self._send_parking_message_flag

    @send_parking_message_flag.setter
    def send_parking_message_flag(self, value):
        self._send_parking_message_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportParkingPaymentinfoSyncResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'send_parking_message_flag' in response:
            self.send_parking_message_flag = response['send_parking_message_flag']
