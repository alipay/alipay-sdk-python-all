#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleRiskConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleRiskConsultResponse, self).__init__()
        self._risk_level = None

    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleRiskConsultResponse, self).parse_response_content(response_content)
        if 'risk_level' in response:
            self.risk_level = response['risk_level']
