#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaasAccountInfo import SaasAccountInfo


class AlipayTradeSaasAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasAccountQueryResponse, self).__init__()
        self._account_list = None
        self._customer_id = None

    @property
    def account_list(self):
        return self._account_list

    @account_list.setter
    def account_list(self, value):
        if isinstance(value, list):
            self._account_list = list()
            for i in value:
                if isinstance(i, SaasAccountInfo):
                    self._account_list.append(i)
                else:
                    self._account_list.append(SaasAccountInfo.from_alipay_dict(i))
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasAccountQueryResponse, self).parse_response_content(response_content)
        if 'account_list' in response:
            self.account_list = response['account_list']
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
