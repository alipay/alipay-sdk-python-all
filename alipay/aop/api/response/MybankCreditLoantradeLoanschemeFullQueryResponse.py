#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Contract import Contract
from alipay.aop.api.domain.LoanScheme import LoanScheme
from alipay.aop.api.domain.MyBkAccountVO import MyBkAccountVO
from alipay.aop.api.domain.MyBkAccountVO import MyBkAccountVO


class MybankCreditLoantradeLoanschemeFullQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanschemeFullQueryResponse, self).__init__()
        self._contract_list = None
        self._data_sign = None
        self._loan_scheme = None
        self._repay_account = None
        self._trans_in_account = None

    @property
    def contract_list(self):
        return self._contract_list

    @contract_list.setter
    def contract_list(self, value):
        if isinstance(value, list):
            self._contract_list = list()
            for i in value:
                if isinstance(i, Contract):
                    self._contract_list.append(i)
                else:
                    self._contract_list.append(Contract.from_alipay_dict(i))
    @property
    def data_sign(self):
        return self._data_sign

    @data_sign.setter
    def data_sign(self, value):
        self._data_sign = value
    @property
    def loan_scheme(self):
        return self._loan_scheme

    @loan_scheme.setter
    def loan_scheme(self, value):
        if isinstance(value, LoanScheme):
            self._loan_scheme = value
        else:
            self._loan_scheme = LoanScheme.from_alipay_dict(value)
    @property
    def repay_account(self):
        return self._repay_account

    @repay_account.setter
    def repay_account(self, value):
        if isinstance(value, MyBkAccountVO):
            self._repay_account = value
        else:
            self._repay_account = MyBkAccountVO.from_alipay_dict(value)
    @property
    def trans_in_account(self):
        return self._trans_in_account

    @trans_in_account.setter
    def trans_in_account(self, value):
        if isinstance(value, MyBkAccountVO):
            self._trans_in_account = value
        else:
            self._trans_in_account = MyBkAccountVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanschemeFullQueryResponse, self).parse_response_content(response_content)
        if 'contract_list' in response:
            self.contract_list = response['contract_list']
        if 'data_sign' in response:
            self.data_sign = response['data_sign']
        if 'loan_scheme' in response:
            self.loan_scheme = response['loan_scheme']
        if 'repay_account' in response:
            self.repay_account = response['repay_account']
        if 'trans_in_account' in response:
            self.trans_in_account = response['trans_in_account']
