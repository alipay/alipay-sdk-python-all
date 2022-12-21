#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCertificationRiskIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCertificationRiskIdentifyResponse, self).__init__()
        self._risk_identify_result = None
        self._shell_company_level = None

    @property
    def risk_identify_result(self):
        return self._risk_identify_result

    @risk_identify_result.setter
    def risk_identify_result(self, value):
        if isinstance(value, list):
            self._risk_identify_result = list()
            for i in value:
                self._risk_identify_result.append(i)
    @property
    def shell_company_level(self):
        return self._shell_company_level

    @shell_company_level.setter
    def shell_company_level(self, value):
        self._shell_company_level = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCertificationRiskIdentifyResponse, self).parse_response_content(response_content)
        if 'risk_identify_result' in response:
            self.risk_identify_result = response['risk_identify_result']
        if 'shell_company_level' in response:
            self.shell_company_level = response['shell_company_level']
