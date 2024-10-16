#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantSolcreditserviceprodProductCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolcreditserviceprodProductCreateormodifyResponse, self).__init__()
        self._product_no = None

    @property
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolcreditserviceprodProductCreateormodifyResponse, self).parse_response_content(response_content)
        if 'product_no' in response:
            self.product_no = response['product_no']
