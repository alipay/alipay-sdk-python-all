#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankStagedThresholdInfo import DtBankStagedThresholdInfo


class DtBankPreferenceMultiStagedRule(object):

    def __init__(self):
        self._max_reduce_amount = None
        self._staged_discount_list = None

    @property
    def max_reduce_amount(self):
        return self._max_reduce_amount

    @max_reduce_amount.setter
    def max_reduce_amount(self, value):
        self._max_reduce_amount = value
    @property
    def staged_discount_list(self):
        return self._staged_discount_list

    @staged_discount_list.setter
    def staged_discount_list(self, value):
        if isinstance(value, list):
            self._staged_discount_list = list()
            for i in value:
                if isinstance(i, DtBankStagedThresholdInfo):
                    self._staged_discount_list.append(i)
                else:
                    self._staged_discount_list.append(DtBankStagedThresholdInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.max_reduce_amount:
            if hasattr(self.max_reduce_amount, 'to_alipay_dict'):
                params['max_reduce_amount'] = self.max_reduce_amount.to_alipay_dict()
            else:
                params['max_reduce_amount'] = self.max_reduce_amount
        if self.staged_discount_list:
            if isinstance(self.staged_discount_list, list):
                for i in range(0, len(self.staged_discount_list)):
                    element = self.staged_discount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.staged_discount_list[i] = element.to_alipay_dict()
            if hasattr(self.staged_discount_list, 'to_alipay_dict'):
                params['staged_discount_list'] = self.staged_discount_list.to_alipay_dict()
            else:
                params['staged_discount_list'] = self.staged_discount_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankPreferenceMultiStagedRule()
        if 'max_reduce_amount' in d:
            o.max_reduce_amount = d['max_reduce_amount']
        if 'staged_discount_list' in d:
            o.staged_discount_list = d['staged_discount_list']
        return o


