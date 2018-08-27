#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdFingerprintRiskcontrolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFingerprintRiskcontrolQueryResponse, self).__init__()
        self._check_result = None

    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFingerprintRiskcontrolQueryResponse, self).parse_response_content(response_content)
        if 'check_result' in response:
            self.check_result = response['check_result']
