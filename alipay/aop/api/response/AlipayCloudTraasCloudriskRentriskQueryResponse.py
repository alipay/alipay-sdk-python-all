#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentRiskResult import RentRiskResult


class AlipayCloudTraasCloudriskRentriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudTraasCloudriskRentriskQueryResponse, self).__init__()
        self._risk_result = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        if isinstance(value, RentRiskResult):
            self._risk_result = value
        else:
            self._risk_result = RentRiskResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudTraasCloudriskRentriskQueryResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
