#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainFactoringSupplierCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainFactoringSupplierCreateResponse, self).__init__()
        self._supplier_no = None

    @property
    def supplier_no(self):
        return self._supplier_no

    @supplier_no.setter
    def supplier_no(self, value):
        self._supplier_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainFactoringSupplierCreateResponse, self).parse_response_content(response_content)
        if 'supplier_no' in response:
            self.supplier_no = response['supplier_no']
