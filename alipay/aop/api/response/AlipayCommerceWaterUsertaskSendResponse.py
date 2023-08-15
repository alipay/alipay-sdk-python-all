#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWaterUsertaskSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterUsertaskSendResponse, self).__init__()
        self._trigger_result = None

    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        self._trigger_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterUsertaskSendResponse, self).parse_response_content(response_content)
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
