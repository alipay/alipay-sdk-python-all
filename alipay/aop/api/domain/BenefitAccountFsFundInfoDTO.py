#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitAccountRepayBankInfoDTO import BenefitAccountRepayBankInfoDTO


class BenefitAccountFsFundInfoDTO(object):

    def __init__(self):
        self._amount = None
        self._current_amount = None
        self._fund_principal = None
        self._fund_provider = None
        self._fund_type = None
        self._fund_user_id = None
        self._repay_bank_info = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def current_amount(self):
        return self._current_amount

    @current_amount.setter
    def current_amount(self, value):
        self._current_amount = value
    @property
    def fund_principal(self):
        return self._fund_principal

    @fund_principal.setter
    def fund_principal(self, value):
        self._fund_principal = value
    @property
    def fund_provider(self):
        return self._fund_provider

    @fund_provider.setter
    def fund_provider(self, value):
        self._fund_provider = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def fund_user_id(self):
        return self._fund_user_id

    @fund_user_id.setter
    def fund_user_id(self, value):
        self._fund_user_id = value
    @property
    def repay_bank_info(self):
        return self._repay_bank_info

    @repay_bank_info.setter
    def repay_bank_info(self, value):
        if isinstance(value, BenefitAccountRepayBankInfoDTO):
            self._repay_bank_info = value
        else:
            self._repay_bank_info = BenefitAccountRepayBankInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.current_amount:
            if hasattr(self.current_amount, 'to_alipay_dict'):
                params['current_amount'] = self.current_amount.to_alipay_dict()
            else:
                params['current_amount'] = self.current_amount
        if self.fund_principal:
            if hasattr(self.fund_principal, 'to_alipay_dict'):
                params['fund_principal'] = self.fund_principal.to_alipay_dict()
            else:
                params['fund_principal'] = self.fund_principal
        if self.fund_provider:
            if hasattr(self.fund_provider, 'to_alipay_dict'):
                params['fund_provider'] = self.fund_provider.to_alipay_dict()
            else:
                params['fund_provider'] = self.fund_provider
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.fund_user_id:
            if hasattr(self.fund_user_id, 'to_alipay_dict'):
                params['fund_user_id'] = self.fund_user_id.to_alipay_dict()
            else:
                params['fund_user_id'] = self.fund_user_id
        if self.repay_bank_info:
            if hasattr(self.repay_bank_info, 'to_alipay_dict'):
                params['repay_bank_info'] = self.repay_bank_info.to_alipay_dict()
            else:
                params['repay_bank_info'] = self.repay_bank_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitAccountFsFundInfoDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'current_amount' in d:
            o.current_amount = d['current_amount']
        if 'fund_principal' in d:
            o.fund_principal = d['fund_principal']
        if 'fund_provider' in d:
            o.fund_provider = d['fund_provider']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'fund_user_id' in d:
            o.fund_user_id = d['fund_user_id']
        if 'repay_bank_info' in d:
            o.repay_bank_info = d['repay_bank_info']
        return o


