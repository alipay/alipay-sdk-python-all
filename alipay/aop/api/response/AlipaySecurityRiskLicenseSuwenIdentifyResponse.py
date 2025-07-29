#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskLicenseSuwenIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskLicenseSuwenIdentifyResponse, self).__init__()
        self._suwen_event_id = None

    @property
    def suwen_event_id(self):
        return self._suwen_event_id

    @suwen_event_id.setter
    def suwen_event_id(self, value):
        self._suwen_event_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskLicenseSuwenIdentifyResponse, self).parse_response_content(response_content)
        if 'suwen_event_id' in response:
            self.suwen_event_id = response['suwen_event_id']
