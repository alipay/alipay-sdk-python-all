#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcCardapplyNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcCardapplyNotifyResponse, self).__init__()
        self._notify_result = None

    @property
    def notify_result(self):
        return self._notify_result

    @notify_result.setter
    def notify_result(self, value):
        self._notify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcCardapplyNotifyResponse, self).parse_response_content(response_content)
        if 'notify_result' in response:
            self.notify_result = response['notify_result']
