#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMerchantInfoSimpleQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantInfoSimpleQueryResponse, self).__init__()
        self._operator_prefix = None
        self._partner_id = None
        self._user_name = None

    @property
    def operator_prefix(self):
        return self._operator_prefix

    @operator_prefix.setter
    def operator_prefix(self, value):
        self._operator_prefix = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantInfoSimpleQueryResponse, self).parse_response_content(response_content)
        if 'operator_prefix' in response:
            self.operator_prefix = response['operator_prefix']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
