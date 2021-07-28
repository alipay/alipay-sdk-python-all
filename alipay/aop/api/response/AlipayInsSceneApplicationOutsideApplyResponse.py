#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneApplicationOutsideApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationOutsideApplyResponse, self).__init__()
        self._out_biz_no = None
        self._policy_no = None
        self._premium = None
        self._risk_level = None
        self._sum_insured = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationOutsideApplyResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'premium' in response:
            self.premium = response['premium']
        if 'risk_level' in response:
            self.risk_level = response['risk_level']
        if 'sum_insured' in response:
            self.sum_insured = response['sum_insured']
