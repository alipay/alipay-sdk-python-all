#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskStrategy import RiskStrategy


class ZhimaCreditEpRiskInfoIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpRiskInfoIdentifyResponse, self).__init__()
        self._risk_strategy_list = None

    @property
    def risk_strategy_list(self):
        return self._risk_strategy_list

    @risk_strategy_list.setter
    def risk_strategy_list(self, value):
        if isinstance(value, list):
            self._risk_strategy_list = list()
            for i in value:
                if isinstance(i, RiskStrategy):
                    self._risk_strategy_list.append(i)
                else:
                    self._risk_strategy_list.append(RiskStrategy.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpRiskInfoIdentifyResponse, self).parse_response_content(response_content)
        if 'risk_strategy_list' in response:
            self.risk_strategy_list = response['risk_strategy_list']
