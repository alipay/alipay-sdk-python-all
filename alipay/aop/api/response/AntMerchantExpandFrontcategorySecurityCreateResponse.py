#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandFrontcategorySecurityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandFrontcategorySecurityCreateResponse, self).__init__()
        self._front_category_id = None

    @property
    def front_category_id(self):
        return self._front_category_id

    @front_category_id.setter
    def front_category_id(self, value):
        self._front_category_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandFrontcategorySecurityCreateResponse, self).parse_response_content(response_content)
        if 'front_category_id' in response:
            self.front_category_id = response['front_category_id']
