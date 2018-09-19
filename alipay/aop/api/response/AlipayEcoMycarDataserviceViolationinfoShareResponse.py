#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarDataserviceViolationinfoShareResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDataserviceViolationinfoShareResponse, self).__init__()
        self._body_num = None
        self._engine_num = None
        self._vehicle_id = None
        self._vi_number = None

    @property
    def body_num(self):
        return self._body_num

    @body_num.setter
    def body_num(self, value):
        self._body_num = value
    @property
    def engine_num(self):
        return self._engine_num

    @engine_num.setter
    def engine_num(self, value):
        self._engine_num = value
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDataserviceViolationinfoShareResponse, self).parse_response_content(response_content)
        if 'body_num' in response:
            self.body_num = response['body_num']
        if 'engine_num' in response:
            self.engine_num = response['engine_num']
        if 'vehicle_id' in response:
            self.vehicle_id = response['vehicle_id']
        if 'vi_number' in response:
            self.vi_number = response['vi_number']
