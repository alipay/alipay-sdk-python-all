#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalBenefitInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalBenefitInfoQueryResponse, self).__init__()
        self._benefit_id = None
        self._can_sell = None
        self._out_benefit_id = None
        self._sku_info = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def out_benefit_id(self):
        return self._out_benefit_id

    @out_benefit_id.setter
    def out_benefit_id(self, value):
        self._out_benefit_id = value
    @property
    def sku_info(self):
        return self._sku_info

    @sku_info.setter
    def sku_info(self, value):
        self._sku_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalBenefitInfoQueryResponse, self).parse_response_content(response_content)
        if 'benefit_id' in response:
            self.benefit_id = response['benefit_id']
        if 'can_sell' in response:
            self.can_sell = response['can_sell']
        if 'out_benefit_id' in response:
            self.out_benefit_id = response['out_benefit_id']
        if 'sku_info' in response:
            self.sku_info = response['sku_info']
