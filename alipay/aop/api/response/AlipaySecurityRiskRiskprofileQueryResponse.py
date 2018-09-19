#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskProfileDto import RiskProfileDto


class AlipaySecurityRiskRiskprofileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskRiskprofileQueryResponse, self).__init__()
        self._message = None
        self._risk_profile_value = None
        self._success = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def risk_profile_value(self):
        return self._risk_profile_value

    @risk_profile_value.setter
    def risk_profile_value(self, value):
        if isinstance(value, list):
            self._risk_profile_value = list()
            for i in value:
                if isinstance(i, RiskProfileDto):
                    self._risk_profile_value.append(i)
                else:
                    self._risk_profile_value.append(RiskProfileDto.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskRiskprofileQueryResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
        if 'risk_profile_value' in response:
            self.risk_profile_value = response['risk_profile_value']
        if 'success' in response:
            self.success = response['success']
