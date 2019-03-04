#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneProductAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneProductAgreementSignResponse, self).__init__()
        self._product_sign_no = None
        self._sign_result = None

    @property
    def product_sign_no(self):
        return self._product_sign_no

    @product_sign_no.setter
    def product_sign_no(self, value):
        self._product_sign_no = value
    @property
    def sign_result(self):
        return self._sign_result

    @sign_result.setter
    def sign_result(self, value):
        self._sign_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneProductAgreementSignResponse, self).parse_response_content(response_content)
        if 'product_sign_no' in response:
            self.product_sign_no = response['product_sign_no']
        if 'sign_result' in response:
            self.sign_result = response['sign_result']
