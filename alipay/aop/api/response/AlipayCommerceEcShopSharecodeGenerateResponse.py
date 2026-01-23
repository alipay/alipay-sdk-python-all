#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcShopSharecodeGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcShopSharecodeGenerateResponse, self).__init__()
        self._share_code = None

    @property
    def share_code(self):
        return self._share_code

    @share_code.setter
    def share_code(self, value):
        self._share_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcShopSharecodeGenerateResponse, self).parse_response_content(response_content)
        if 'share_code' in response:
            self.share_code = response['share_code']
