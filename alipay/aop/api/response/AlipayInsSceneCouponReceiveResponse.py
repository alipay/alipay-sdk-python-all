#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsSceneCouponReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneCouponReceiveResponse, self).__init__()
        self._policy_no = None
        self._product = None

    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, InsProduct):
            self._product = value
        else:
            self._product = InsProduct.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneCouponReceiveResponse, self).parse_response_content(response_content)
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'product' in response:
            self.product = response['product']
