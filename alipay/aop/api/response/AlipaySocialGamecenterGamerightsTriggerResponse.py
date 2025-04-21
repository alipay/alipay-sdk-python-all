#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialGamecenterGamerightsTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialGamecenterGamerightsTriggerResponse, self).__init__()
        self._can_not_trigger_reason = None
        self._trigger_success = None

    @property
    def can_not_trigger_reason(self):
        return self._can_not_trigger_reason

    @can_not_trigger_reason.setter
    def can_not_trigger_reason(self, value):
        self._can_not_trigger_reason = value
    @property
    def trigger_success(self):
        return self._trigger_success

    @trigger_success.setter
    def trigger_success(self, value):
        self._trigger_success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialGamecenterGamerightsTriggerResponse, self).parse_response_content(response_content)
        if 'can_not_trigger_reason' in response:
            self.can_not_trigger_reason = response['can_not_trigger_reason']
        if 'trigger_success' in response:
            self.trigger_success = response['trigger_success']
