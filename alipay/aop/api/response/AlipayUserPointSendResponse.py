#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserPointSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPointSendResponse, self).__init__()
        self._send_point = None

    @property
    def send_point(self):
        return self._send_point

    @send_point.setter
    def send_point(self, value):
        self._send_point = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserPointSendResponse, self).parse_response_content(response_content)
        if 'send_point' in response:
            self.send_point = response['send_point']
