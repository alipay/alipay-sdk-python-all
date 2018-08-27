#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthContractMerchantUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthContractMerchantUnsignResponse, self).__init__()
        self._contract_batch_no_list = None
        self._contract_no_list = None

    @property
    def contract_batch_no_list(self):
        return self._contract_batch_no_list

    @contract_batch_no_list.setter
    def contract_batch_no_list(self, value):
        if isinstance(value, list):
            self._contract_batch_no_list = list()
            for i in value:
                self._contract_batch_no_list.append(i)
    @property
    def contract_no_list(self):
        return self._contract_no_list

    @contract_no_list.setter
    def contract_no_list(self, value):
        if isinstance(value, list):
            self._contract_no_list = list()
            for i in value:
                self._contract_no_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthContractMerchantUnsignResponse, self).parse_response_content(response_content)
        if 'contract_batch_no_list' in response:
            self.contract_batch_no_list = response['contract_batch_no_list']
        if 'contract_no_list' in response:
            self.contract_no_list = response['contract_no_list']
