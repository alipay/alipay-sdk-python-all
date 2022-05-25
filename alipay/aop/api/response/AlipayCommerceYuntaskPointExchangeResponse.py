#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskPointExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskPointExchangeResponse, self).__init__()
        self._instruction_id = None
        self._messsage = None
        self._point = None
        self._result = None

    @property
    def instruction_id(self):
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, value):
        self._instruction_id = value
    @property
    def messsage(self):
        return self._messsage

    @messsage.setter
    def messsage(self, value):
        self._messsage = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskPointExchangeResponse, self).parse_response_content(response_content)
        if 'instruction_id' in response:
            self.instruction_id = response['instruction_id']
        if 'messsage' in response:
            self.messsage = response['messsage']
        if 'point' in response:
            self.point = response['point']
        if 'result' in response:
            self.result = response['result']
