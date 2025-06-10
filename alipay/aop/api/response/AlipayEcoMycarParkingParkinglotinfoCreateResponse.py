#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingParkinglotinfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingParkinglotinfoCreateResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._parking_id = None

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
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingParkinglotinfoCreateResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'parking_id' in response:
            self.parking_id = response['parking_id']
