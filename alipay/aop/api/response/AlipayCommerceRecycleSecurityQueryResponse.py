#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleSecurityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleSecurityQueryResponse, self).__init__()
        self._risk_level = None
        self._risk_reason = None

    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_reason(self):
        return self._risk_reason

    @risk_reason.setter
    def risk_reason(self, value):
        self._risk_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleSecurityQueryResponse, self).parse_response_content(response_content)
        if 'risk_level' in response:
            self.risk_level = response['risk_level']
        if 'risk_reason' in response:
            self.risk_reason = response['risk_reason']
