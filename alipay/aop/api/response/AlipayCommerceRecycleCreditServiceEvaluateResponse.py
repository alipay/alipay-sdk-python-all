#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRecycleCreditServiceEvaluateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleCreditServiceEvaluateResponse, self).__init__()
        self._permit = None
        self._pre_settlement_ratio = None
        self._risk_order_no = None

    @property
    def permit(self):
        return self._permit

    @permit.setter
    def permit(self, value):
        self._permit = value
    @property
    def pre_settlement_ratio(self):
        return self._pre_settlement_ratio

    @pre_settlement_ratio.setter
    def pre_settlement_ratio(self, value):
        self._pre_settlement_ratio = value
    @property
    def risk_order_no(self):
        return self._risk_order_no

    @risk_order_no.setter
    def risk_order_no(self, value):
        self._risk_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleCreditServiceEvaluateResponse, self).parse_response_content(response_content)
        if 'permit' in response:
            self.permit = response['permit']
        if 'pre_settlement_ratio' in response:
            self.pre_settlement_ratio = response['pre_settlement_ratio']
        if 'risk_order_no' in response:
            self.risk_order_no = response['risk_order_no']
