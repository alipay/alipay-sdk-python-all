#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceBroadcastQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceBroadcastQueryResponse, self).__init__()
        self._broadcast_time = None
        self._result = None

    @property
    def broadcast_time(self):
        return self._broadcast_time

    @broadcast_time.setter
    def broadcast_time(self, value):
        self._broadcast_time = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceBroadcastQueryResponse, self).parse_response_content(response_content)
        if 'broadcast_time' in response:
            self.broadcast_time = response['broadcast_time']
        if 'result' in response:
            self.result = response['result']
