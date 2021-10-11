#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainTwcCertifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainTwcCertifyQueryResponse, self).__init__()
        self._passed = None

    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainTwcCertifyQueryResponse, self).parse_response_content(response_content)
        if 'passed' in response:
            self.passed = response['passed']
