#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecomProduct import RecomProduct


class AlipayInsMarketingProductRecommendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingProductRecommendResponse, self).__init__()
        self._products = None
        self._recom_flow_no = None

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        if isinstance(value, list):
            self._products = list()
            for i in value:
                if isinstance(i, RecomProduct):
                    self._products.append(i)
                else:
                    self._products.append(RecomProduct.from_alipay_dict(i))
    @property
    def recom_flow_no(self):
        return self._recom_flow_no

    @recom_flow_no.setter
    def recom_flow_no(self, value):
        self._recom_flow_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingProductRecommendResponse, self).parse_response_content(response_content)
        if 'products' in response:
            self.products = response['products']
        if 'recom_flow_no' in response:
            self.recom_flow_no = response['recom_flow_no']
