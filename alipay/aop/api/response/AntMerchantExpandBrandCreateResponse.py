#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandBrandCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandBrandCreateResponse, self).__init__()
        self._brand_id = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandBrandCreateResponse, self).parse_response_content(response_content)
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
