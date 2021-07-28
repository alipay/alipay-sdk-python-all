#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PurchaseApplyInfoDTO import PurchaseApplyInfoDTO


class BizBudgetDTO(object):

    def __init__(self):
        self._available_amount = None
        self._biz_apply_info = None
        self._biz_budget_id = None
        self._biz_budget_name = None
        self._currency = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def biz_apply_info(self):
        return self._biz_apply_info

    @biz_apply_info.setter
    def biz_apply_info(self, value):
        if isinstance(value, list):
            self._biz_apply_info = list()
            for i in value:
                if isinstance(i, PurchaseApplyInfoDTO):
                    self._biz_apply_info.append(i)
                else:
                    self._biz_apply_info.append(PurchaseApplyInfoDTO.from_alipay_dict(i))
    @property
    def biz_budget_id(self):
        return self._biz_budget_id

    @biz_budget_id.setter
    def biz_budget_id(self, value):
        self._biz_budget_id = value
    @property
    def biz_budget_name(self):
        return self._biz_budget_name

    @biz_budget_name.setter
    def biz_budget_name(self, value):
        self._biz_budget_name = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.biz_apply_info:
            if isinstance(self.biz_apply_info, list):
                for i in range(0, len(self.biz_apply_info)):
                    element = self.biz_apply_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_apply_info[i] = element.to_alipay_dict()
            if hasattr(self.biz_apply_info, 'to_alipay_dict'):
                params['biz_apply_info'] = self.biz_apply_info.to_alipay_dict()
            else:
                params['biz_apply_info'] = self.biz_apply_info
        if self.biz_budget_id:
            if hasattr(self.biz_budget_id, 'to_alipay_dict'):
                params['biz_budget_id'] = self.biz_budget_id.to_alipay_dict()
            else:
                params['biz_budget_id'] = self.biz_budget_id
        if self.biz_budget_name:
            if hasattr(self.biz_budget_name, 'to_alipay_dict'):
                params['biz_budget_name'] = self.biz_budget_name.to_alipay_dict()
            else:
                params['biz_budget_name'] = self.biz_budget_name
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizBudgetDTO()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'biz_apply_info' in d:
            o.biz_apply_info = d['biz_apply_info']
        if 'biz_budget_id' in d:
            o.biz_budget_id = d['biz_budget_id']
        if 'biz_budget_name' in d:
            o.biz_budget_name = d['biz_budget_name']
        if 'currency' in d:
            o.currency = d['currency']
        return o


