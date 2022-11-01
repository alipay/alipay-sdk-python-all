#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletTemplateConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletTemplateConfirmResponse, self).__init__()
        self._biz_scene = None
        self._product_code = None
        self._wallet_template_id = None

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
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletTemplateConfirmResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'wallet_template_id' in response:
            self.wallet_template_id = response['wallet_template_id']
