#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialGamecenterGamerightsConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialGamecenterGamerightsConsultResponse, self).__init__()
        self._can_not_trigger_reason = None
        self._can_trigger = None

    @property
    def can_not_trigger_reason(self):
        return self._can_not_trigger_reason

    @can_not_trigger_reason.setter
    def can_not_trigger_reason(self, value):
        self._can_not_trigger_reason = value
    @property
    def can_trigger(self):
        return self._can_trigger

    @can_trigger.setter
    def can_trigger(self, value):
        self._can_trigger = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialGamecenterGamerightsConsultResponse, self).parse_response_content(response_content)
        if 'can_not_trigger_reason' in response:
            self.can_not_trigger_reason = response['can_not_trigger_reason']
        if 'can_trigger' in response:
            self.can_trigger = response['can_trigger']
