#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskImagePlusQueryResult import RiskImagePlusQueryResult


class AlipayCloudTraasRiskgoFarmingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudTraasRiskgoFarmingQueryResponse, self).__init__()
        self._risk_result = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        if isinstance(value, list):
            self._risk_result = list()
            for i in value:
                if isinstance(i, RiskImagePlusQueryResult):
                    self._risk_result.append(i)
                else:
                    self._risk_result.append(RiskImagePlusQueryResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudTraasRiskgoFarmingQueryResponse, self).parse_response_content(response_content)
        if 'risk_result' in response:
            self.risk_result = response['risk_result']
