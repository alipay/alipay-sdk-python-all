#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCertificationRiskIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCertificationRiskIdentifyResponse, self).__init__()
        self._risk_identify_result = None

    @property
    def risk_identify_result(self):
        return self._risk_identify_result

    @risk_identify_result.setter
    def risk_identify_result(self, value):
        if isinstance(value, list):
            self._risk_identify_result = list()
            for i in value:
                self._risk_identify_result.append(i)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCertificationRiskIdentifyResponse, self).parse_response_content(response_content)
        if 'risk_identify_result' in response:
            self.risk_identify_result = response['risk_identify_result']
