#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PrizeInstanceInfo import PrizeInstanceInfo


class AlipayCommerceRetailActivitySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailActivitySendResponse, self).__init__()
        self._prize_instance_info = None
        self._send_success = None

    @property
    def prize_instance_info(self):
        return self._prize_instance_info

    @prize_instance_info.setter
    def prize_instance_info(self, value):
        if isinstance(value, PrizeInstanceInfo):
            self._prize_instance_info = value
        else:
            self._prize_instance_info = PrizeInstanceInfo.from_alipay_dict(value)
    @property
    def send_success(self):
        return self._send_success

    @send_success.setter
    def send_success(self, value):
        self._send_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailActivitySendResponse, self).parse_response_content(response_content)
        if 'prize_instance_info' in response:
            self.prize_instance_info = response['prize_instance_info']
        if 'send_success' in response:
            self.send_success = response['send_success']
