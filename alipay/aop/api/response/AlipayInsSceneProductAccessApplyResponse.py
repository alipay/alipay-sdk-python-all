#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsSceneProductAccessApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneProductAccessApplyResponse, self).__init__()
        self._is_access = None
        self._product = None
        self._reason = None

    @property
    def is_access(self):
        return self._is_access

    @is_access.setter
    def is_access(self, value):
        self._is_access = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, InsProduct):
            self._product = value
        else:
            self._product = InsProduct.from_alipay_dict(value)
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneProductAccessApplyResponse, self).parse_response_content(response_content)
        if 'is_access' in response:
            self.is_access = response['is_access']
        if 'product' in response:
            self.product = response['product']
        if 'reason' in response:
            self.reason = response['reason']
