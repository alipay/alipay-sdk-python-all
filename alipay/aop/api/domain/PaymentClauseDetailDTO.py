#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WitnessPrincipalDTO import WitnessPrincipalDTO
from alipay.aop.api.domain.WitnessPrincipalDTO import WitnessPrincipalDTO


class PaymentClauseDetailDTO(object):

    def __init__(self):
        self._amount = None
        self._memo = None
        self._trans_in_principal = None
        self._trans_out_principal = None

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
    def trans_in_principal(self):
        return self._trans_in_principal

    @trans_in_principal.setter
    def trans_in_principal(self, value):
        if isinstance(value, WitnessPrincipalDTO):
            self._trans_in_principal = value
        else:
            self._trans_in_principal = WitnessPrincipalDTO.from_alipay_dict(value)
    @property
    def trans_out_principal(self):
        return self._trans_out_principal

    @trans_out_principal.setter
    def trans_out_principal(self, value):
        if isinstance(value, WitnessPrincipalDTO):
            self._trans_out_principal = value
        else:
            self._trans_out_principal = WitnessPrincipalDTO.from_alipay_dict(value)


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
        if self.trans_in_principal:
            if hasattr(self.trans_in_principal, 'to_alipay_dict'):
                params['trans_in_principal'] = self.trans_in_principal.to_alipay_dict()
            else:
                params['trans_in_principal'] = self.trans_in_principal
        if self.trans_out_principal:
            if hasattr(self.trans_out_principal, 'to_alipay_dict'):
                params['trans_out_principal'] = self.trans_out_principal.to_alipay_dict()
            else:
                params['trans_out_principal'] = self.trans_out_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentClauseDetailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'trans_in_principal' in d:
            o.trans_in_principal = d['trans_in_principal']
        if 'trans_out_principal' in d:
            o.trans_out_principal = d['trans_out_principal']
        return o


