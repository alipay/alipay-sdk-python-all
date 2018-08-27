#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskRankInfoCode import RiskRankInfoCode


class AlipaySecurityRiskCustomerriskrankGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskCustomerriskrankGetResponse, self).__init__()
        self._has_risk = None
        self._info_code = None
        self._risk_rank = None
        self._risk_score = None

    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value
    @property
    def info_code(self):
        return self._info_code

    @info_code.setter
    def info_code(self, value):
        if isinstance(value, list):
            self._info_code = list()
            for i in value:
                if isinstance(i, RiskRankInfoCode):
                    self._info_code.append(i)
                else:
                    self._info_code.append(RiskRankInfoCode.from_alipay_dict(i))
    @property
    def risk_rank(self):
        return self._risk_rank

    @risk_rank.setter
    def risk_rank(self, value):
        self._risk_rank = value
    @property
    def risk_score(self):
        return self._risk_score

    @risk_score.setter
    def risk_score(self, value):
        self._risk_score = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskCustomerriskrankGetResponse, self).parse_response_content(response_content)
        if 'has_risk' in response:
            self.has_risk = response['has_risk']
        if 'info_code' in response:
            self.info_code = response['info_code']
        if 'risk_rank' in response:
            self.risk_rank = response['risk_rank']
        if 'risk_score' in response:
            self.risk_score = response['risk_score']
