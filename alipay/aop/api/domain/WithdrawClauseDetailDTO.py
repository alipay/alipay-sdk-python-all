#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WitnessPrincipalDTO import WitnessPrincipalDTO
from alipay.aop.api.domain.WithdrawPrincipalDTO import WithdrawPrincipalDTO


class WithdrawClauseDetailDTO(object):

    def __init__(self):
        self._amount = None
        self._memo = None
        self._trans_out_principal = None
        self._withdraw_principal = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def trans_out_principal(self):
        return self._trans_out_principal

    @trans_out_principal.setter
    def trans_out_principal(self, value):
        if isinstance(value, WitnessPrincipalDTO):
            self._trans_out_principal = value
        else:
            self._trans_out_principal = WitnessPrincipalDTO.from_alipay_dict(value)
    @property
    def withdraw_principal(self):
        return self._withdraw_principal

    @withdraw_principal.setter
    def withdraw_principal(self, value):
        if isinstance(value, WithdrawPrincipalDTO):
            self._withdraw_principal = value
        else:
            self._withdraw_principal = WithdrawPrincipalDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.trans_out_principal:
            if hasattr(self.trans_out_principal, 'to_alipay_dict'):
                params['trans_out_principal'] = self.trans_out_principal.to_alipay_dict()
            else:
                params['trans_out_principal'] = self.trans_out_principal
        if self.withdraw_principal:
            if hasattr(self.withdraw_principal, 'to_alipay_dict'):
                params['withdraw_principal'] = self.withdraw_principal.to_alipay_dict()
            else:
                params['withdraw_principal'] = self.withdraw_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithdrawClauseDetailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'trans_out_principal' in d:
            o.trans_out_principal = d['trans_out_principal']
        if 'withdraw_principal' in d:
            o.withdraw_principal = d['withdraw_principal']
        return o


