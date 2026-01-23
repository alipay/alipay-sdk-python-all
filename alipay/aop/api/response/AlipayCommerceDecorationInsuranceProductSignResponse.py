#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignProductVO import SignProductVO


class AlipayCommerceDecorationInsuranceProductSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDecorationInsuranceProductSignResponse, self).__init__()
        self._sign_product_list = None

    @property
    def sign_product_list(self):
        return self._sign_product_list

    @sign_product_list.setter
    def sign_product_list(self, value):
        if isinstance(value, list):
            self._sign_product_list = list()
            for i in value:
                if isinstance(i, SignProductVO):
                    self._sign_product_list.append(i)
                else:
                    self._sign_product_list.append(SignProductVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDecorationInsuranceProductSignResponse, self).parse_response_content(response_content)
        if 'sign_product_list' in response:
            self.sign_product_list = response['sign_product_list']
