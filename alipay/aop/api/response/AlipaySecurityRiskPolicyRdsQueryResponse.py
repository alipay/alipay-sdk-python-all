#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskPolicyRdsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskPolicyRdsQueryResponse, self).__init__()
        self._rds_result = None

    @property
    def rds_result(self):
        return self._rds_result

    @rds_result.setter
    def rds_result(self, value):
        self._rds_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskPolicyRdsQueryResponse, self).parse_response_content(response_content)
        if 'rds_result' in response:
            self.rds_result = response['rds_result']
