#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskDoc import RiskDoc


class ZhimaCreditEpRiskDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRiskDetailQueryResponse, self).__init__()
        self._risk_list = None
        self._total_size = None

    @property
    def risk_list(self):
        return self._risk_list

    @risk_list.setter
    def risk_list(self, value):
        if isinstance(value, RiskDoc):
            self._risk_list = value
        else:
            self._risk_list = RiskDoc.from_alipay_dict(value)
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRiskDetailQueryResponse, self).parse_response_content(response_content)
        if 'risk_list' in response:
            self.risk_list = response['risk_list']
        if 'total_size' in response:
            self.total_size = response['total_size']
