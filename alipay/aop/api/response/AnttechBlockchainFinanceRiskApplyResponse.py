#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceRiskApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceRiskApplyResponse, self).__init__()
        self._out_risk_id = None
        self._risk_info = None

    @property
    def out_risk_id(self):
        return self._out_risk_id

    @out_risk_id.setter
    def out_risk_id(self, value):
        self._out_risk_id = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceRiskApplyResponse, self).parse_response_content(response_content)
        if 'out_risk_id' in response:
            self.out_risk_id = response['out_risk_id']
        if 'risk_info' in response:
            self.risk_info = response['risk_info']
