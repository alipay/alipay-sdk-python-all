#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTaxbillSigncodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTaxbillSigncodeCreateResponse, self).__init__()
        self._biz_scene = None
        self._product_code = None
        self._sign_code = None
        self._sign_code_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sign_code(self):
        return self._sign_code

    @sign_code.setter
    def sign_code(self, value):
        self._sign_code = value
    @property
    def sign_code_type(self):
        return self._sign_code_type

    @sign_code_type.setter
    def sign_code_type(self, value):
        self._sign_code_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTaxbillSigncodeCreateResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'sign_code' in response:
            self.sign_code = response['sign_code']
        if 'sign_code_type' in response:
            self.sign_code_type = response['sign_code_type']
