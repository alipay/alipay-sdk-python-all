#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseReliableCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseReliableCreateResponse, self).__init__()
        self._account_id = None
        self._enterprise_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseReliableCreateResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'enterprise_id' in response:
            self.enterprise_id = response['enterprise_id']
