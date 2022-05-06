#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountBaseInfoVO import AccountBaseInfoVO


class AlipayFinancialnetAccountlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAccountlistQueryResponse, self).__init__()
        self._account_infos = None
        self._result_code = None
        self._result_desc = None
        self._success = None

    @property
    def account_infos(self):
        return self._account_infos

    @account_infos.setter
    def account_infos(self, value):
        if isinstance(value, list):
            self._account_infos = list()
            for i in value:
                if isinstance(i, AccountBaseInfoVO):
                    self._account_infos.append(i)
                else:
                    self._account_infos.append(AccountBaseInfoVO.from_alipay_dict(i))
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAccountlistQueryResponse, self).parse_response_content(response_content)
        if 'account_infos' in response:
            self.account_infos = response['account_infos']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'success' in response:
            self.success = response['success']
