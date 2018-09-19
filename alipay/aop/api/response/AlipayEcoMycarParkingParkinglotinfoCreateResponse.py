#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingParkinglotinfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingParkinglotinfoCreateResponse, self).__init__()
        self._parking_id = None

    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingParkinglotinfoCreateResponse, self).parse_response_content(response_content)
        if 'parking_id' in response:
            self.parking_id = response['parking_id']
