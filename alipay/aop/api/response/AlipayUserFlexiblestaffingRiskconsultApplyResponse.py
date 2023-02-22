#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RiskApplyConsult import RiskApplyConsult


class AlipayUserFlexiblestaffingRiskconsultApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFlexiblestaffingRiskconsultApplyResponse, self).__init__()
        self._biz_scene = None
        self._charge_type = None
        self._out_biz_no = None
        self._product_code = None
        self._risk_results = None
        self._suggest_risk = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def risk_results(self):
        return self._risk_results

    @risk_results.setter
    def risk_results(self, value):
        if isinstance(value, list):
            self._risk_results = list()
            for i in value:
                if isinstance(i, RiskApplyConsult):
                    self._risk_results.append(i)
                else:
                    self._risk_results.append(RiskApplyConsult.from_alipay_dict(i))
    @property
    def suggest_risk(self):
        return self._suggest_risk

    @suggest_risk.setter
    def suggest_risk(self, value):
        self._suggest_risk = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserFlexiblestaffingRiskconsultApplyResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'charge_type' in response:
            self.charge_type = response['charge_type']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'risk_results' in response:
            self.risk_results = response['risk_results']
        if 'suggest_risk' in response:
            self.suggest_risk = response['suggest_risk']
