#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskDeviceinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskDeviceinfoQueryResponse, self).__init__()
        self._atomic_risk = None

    @property
    def atomic_risk(self):
        return self._atomic_risk

    @atomic_risk.setter
    def atomic_risk(self, value):
        self._atomic_risk = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskDeviceinfoQueryResponse, self).parse_response_content(response_content)
        if 'atomic_risk' in response:
            self.atomic_risk = response['atomic_risk']
