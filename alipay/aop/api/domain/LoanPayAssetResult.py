#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.LoanPayInstallment import LoanPayInstallment
from alipay.aop.api.domain.Refuse import Refuse


class LoanPayAssetResult(object):

    def __init__(self):
        self._account_no = None
        self._available_amount = None
        self._enable = None
        self._hint_texts = None
        self._installments = None
        self._refuse_msg = None
        self._scheme_id = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._available_amount = value
        else:
            self._available_amount = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def hint_texts(self):
        return self._hint_texts

    @hint_texts.setter
    def hint_texts(self, value):
        self._hint_texts = value
    @property
    def installments(self):
        return self._installments

    @installments.setter
    def installments(self, value):
        if isinstance(value, list):
            self._installments = list()
            for i in value:
                if isinstance(i, LoanPayInstallment):
                    self._installments.append(i)
                else:
                    self._installments.append(LoanPayInstallment.from_alipay_dict(i))
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        if isinstance(value, Refuse):
            self._refuse_msg = value
        else:
            self._refuse_msg = Refuse.from_alipay_dict(value)
    @property
    def scheme_id(self):
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, value):
        self._scheme_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.hint_texts:
            if hasattr(self.hint_texts, 'to_alipay_dict'):
                params['hint_texts'] = self.hint_texts.to_alipay_dict()
            else:
                params['hint_texts'] = self.hint_texts
        if self.installments:
            if isinstance(self.installments, list):
                for i in range(0, len(self.installments)):
                    element = self.installments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installments[i] = element.to_alipay_dict()
            if hasattr(self.installments, 'to_alipay_dict'):
                params['installments'] = self.installments.to_alipay_dict()
            else:
                params['installments'] = self.installments
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.scheme_id:
            if hasattr(self.scheme_id, 'to_alipay_dict'):
                params['scheme_id'] = self.scheme_id.to_alipay_dict()
            else:
                params['scheme_id'] = self.scheme_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanPayAssetResult()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'enable' in d:
            o.enable = d['enable']
        if 'hint_texts' in d:
            o.hint_texts = d['hint_texts']
        if 'installments' in d:
            o.installments = d['installments']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'scheme_id' in d:
            o.scheme_id = d['scheme_id']
        return o


