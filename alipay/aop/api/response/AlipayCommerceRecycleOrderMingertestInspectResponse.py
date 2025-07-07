#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleAssessProductVO import RecycleAssessProductVO


class AlipayCommerceRecycleOrderMingertestInspectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderMingertestInspectResponse, self).__init__()
        self._assess_product = None

    @property
    def assess_product(self):
        return self._assess_product

    @assess_product.setter
    def assess_product(self, value):
        if isinstance(value, RecycleAssessProductVO):
            self._assess_product = value
        else:
            self._assess_product = RecycleAssessProductVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderMingertestInspectResponse, self).parse_response_content(response_content)
        if 'assess_product' in response:
            self.assess_product = response['assess_product']
