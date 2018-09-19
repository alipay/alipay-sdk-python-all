#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantScreenHit import MerchantScreenHit


class AlipaySecurityProdAmlriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdAmlriskQueryResponse, self).__init__()
        self._event_id = None
        self._has_risk = None
        self._merchant_id = None
        self._risks = None

    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def has_risk(self):
        return self._has_risk

    @has_risk.setter
    def has_risk(self, value):
        self._has_risk = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def risks(self):
        return self._risks

    @risks.setter
    def risks(self, value):
        if isinstance(value, list):
            self._risks = list()
            for i in value:
                if isinstance(i, MerchantScreenHit):
                    self._risks.append(i)
                else:
                    self._risks.append(MerchantScreenHit.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdAmlriskQueryResponse, self).parse_response_content(response_content)
        if 'event_id' in response:
            self.event_id = response['event_id']
        if 'has_risk' in response:
            self.has_risk = response['has_risk']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'risks' in response:
            self.risks = response['risks']
