#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpecialAccountInfo import SpecialAccountInfo


class AlipayCommerceEcRecyclinginvoiceCompanyaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceCompanyaccountQueryResponse, self).__init__()
        self._special_account_info = None
        self._special_account_type = None

    @property
    def special_account_info(self):
        return self._special_account_info

    @special_account_info.setter
    def special_account_info(self, value):
        if isinstance(value, SpecialAccountInfo):
            self._special_account_info = value
        else:
            self._special_account_info = SpecialAccountInfo.from_alipay_dict(value)
    @property
    def special_account_type(self):
        return self._special_account_type

    @special_account_type.setter
    def special_account_type(self, value):
        self._special_account_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceCompanyaccountQueryResponse, self).parse_response_content(response_content)
        if 'special_account_info' in response:
            self.special_account_info = response['special_account_info']
        if 'special_account_type' in response:
            self.special_account_type = response['special_account_type']
