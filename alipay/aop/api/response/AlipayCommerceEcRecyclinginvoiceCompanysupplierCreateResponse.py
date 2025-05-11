#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceCompanysupplierCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceCompanysupplierCreateResponse, self).__init__()
        self._activation_alipay_url = None
        self._activation_url = None
        self._supplier_id = None

    @property
    def activation_alipay_url(self):
        return self._activation_alipay_url

    @activation_alipay_url.setter
    def activation_alipay_url(self, value):
        self._activation_alipay_url = value
    @property
    def activation_url(self):
        return self._activation_url

    @activation_url.setter
    def activation_url(self, value):
        self._activation_url = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceCompanysupplierCreateResponse, self).parse_response_content(response_content)
        if 'activation_alipay_url' in response:
            self.activation_alipay_url = response['activation_alipay_url']
        if 'activation_url' in response:
            self.activation_url = response['activation_url']
        if 'supplier_id' in response:
            self.supplier_id = response['supplier_id']
