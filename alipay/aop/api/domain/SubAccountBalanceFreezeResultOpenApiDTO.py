#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.SubAccountBalanceOpenApiDTO import SubAccountBalanceOpenApiDTO


class SubAccountBalanceFreezeResultOpenApiDTO(object):

    def __init__(self):
        self._freeze_no = None
        self._freeze_success_amount = None
        self._sub_account_balance = None

    @property
    def freeze_no(self):
        return self._freeze_no

    @freeze_no.setter
    def freeze_no(self, value):
        self._freeze_no = value
    @property
    def freeze_success_amount(self):
        return self._freeze_success_amount

    @freeze_success_amount.setter
    def freeze_success_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._freeze_success_amount = value
        else:
            self._freeze_success_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def sub_account_balance(self):
        return self._sub_account_balance

    @sub_account_balance.setter
    def sub_account_balance(self, value):
        if isinstance(value, SubAccountBalanceOpenApiDTO):
            self._sub_account_balance = value
        else:
            self._sub_account_balance = SubAccountBalanceOpenApiDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.freeze_no:
            if hasattr(self.freeze_no, 'to_alipay_dict'):
                params['freeze_no'] = self.freeze_no.to_alipay_dict()
            else:
                params['freeze_no'] = self.freeze_no
        if self.freeze_success_amount:
            if hasattr(self.freeze_success_amount, 'to_alipay_dict'):
                params['freeze_success_amount'] = self.freeze_success_amount.to_alipay_dict()
            else:
                params['freeze_success_amount'] = self.freeze_success_amount
        if self.sub_account_balance:
            if hasattr(self.sub_account_balance, 'to_alipay_dict'):
                params['sub_account_balance'] = self.sub_account_balance.to_alipay_dict()
            else:
                params['sub_account_balance'] = self.sub_account_balance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountBalanceFreezeResultOpenApiDTO()
        if 'freeze_no' in d:
            o.freeze_no = d['freeze_no']
        if 'freeze_success_amount' in d:
            o.freeze_success_amount = d['freeze_success_amount']
        if 'sub_account_balance' in d:
            o.sub_account_balance = d['sub_account_balance']
        return o


