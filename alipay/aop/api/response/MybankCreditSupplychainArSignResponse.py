#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainArSignResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainArSignResponse, self).__init__()
        self._ar_no = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainArSignResponse, self).parse_response_content(response_content)
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
