#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsVoiceEventTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsVoiceEventTriggerResponse, self).__init__()
        self._trigger_id = None

    @property
    def trigger_id(self):
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, value):
        self._trigger_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsVoiceEventTriggerResponse, self).parse_response_content(response_content)
        if 'trigger_id' in response:
            self.trigger_id = response['trigger_id']
