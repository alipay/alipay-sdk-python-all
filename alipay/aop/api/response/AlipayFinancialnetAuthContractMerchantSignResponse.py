#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthContractMerchantSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthContractMerchantSignResponse, self).__init__()
        self._contract_batch_no = None
        self._contract_no_list = None

    @property
    def contract_batch_no(self):
        return self._contract_batch_no

    @contract_batch_no.setter
    def contract_batch_no(self, value):
        self._contract_batch_no = value
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
        response = super(AlipayFinancialnetAuthContractMerchantSignResponse, self).parse_response_content(response_content)
        if 'contract_batch_no' in response:
            self.contract_batch_no = response['contract_batch_no']
        if 'contract_no_list' in response:
            self.contract_no_list = response['contract_no_list']
