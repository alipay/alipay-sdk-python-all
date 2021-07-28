#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdEdgeColorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdEdgeColorQueryResponse, self).__init__()
        self._risk_result = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        self._risk_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdEdgeColorQueryResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
