#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLotteryPresentSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLotteryPresentSendResponse, self).__init__()
        self._send_result = None

    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLotteryPresentSendResponse, self).parse_response_content(response_content)
        if 'send_result' in response:
            self.send_result = response['send_result']
