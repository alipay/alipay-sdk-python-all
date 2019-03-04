#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MTimeControlInfo import MTimeControlInfo
from alipay.aop.api.domain.MItemInfo import MItemInfo
from alipay.aop.api.domain.MTimeControlInfo import MTimeControlInfo


class MEquityUseRule(object):

    def __init__(self):
        self._disabled_times = None
        self._min_cost_amount = None
        self._suit_item_list = None
        self._usaged_times = None

    @property
    def disabled_times(self):
        return self._disabled_times

    @disabled_times.setter
    def disabled_times(self, value):
        if isinstance(value, list):
            self._disabled_times = list()
            for i in value:
                if isinstance(i, MTimeControlInfo):
                    self._disabled_times.append(i)
                else:
                    self._disabled_times.append(MTimeControlInfo.from_alipay_dict(i))
    @property
    def min_cost_amount(self):
        return self._min_cost_amount

    @min_cost_amount.setter
    def min_cost_amount(self, value):
        self._min_cost_amount = value
    @property
    def suit_item_list(self):
        return self._suit_item_list

    @suit_item_list.setter
    def suit_item_list(self, value):
        if isinstance(value, list):
            self._suit_item_list = list()
            for i in value:
                if isinstance(i, MItemInfo):
                    self._suit_item_list.append(i)
                else:
                    self._suit_item_list.append(MItemInfo.from_alipay_dict(i))
    @property
    def usaged_times(self):
        return self._usaged_times

    @usaged_times.setter
    def usaged_times(self, value):
        if isinstance(value, list):
            self._usaged_times = list()
            for i in value:
                if isinstance(i, MTimeControlInfo):
                    self._usaged_times.append(i)
                else:
                    self._usaged_times.append(MTimeControlInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.disabled_times:
            if isinstance(self.disabled_times, list):
                for i in range(0, len(self.disabled_times)):
                    element = self.disabled_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disabled_times[i] = element.to_alipay_dict()
            if hasattr(self.disabled_times, 'to_alipay_dict'):
                params['disabled_times'] = self.disabled_times.to_alipay_dict()
            else:
                params['disabled_times'] = self.disabled_times
        if self.min_cost_amount:
            if hasattr(self.min_cost_amount, 'to_alipay_dict'):
                params['min_cost_amount'] = self.min_cost_amount.to_alipay_dict()
            else:
                params['min_cost_amount'] = self.min_cost_amount
        if self.suit_item_list:
            if isinstance(self.suit_item_list, list):
                for i in range(0, len(self.suit_item_list)):
                    element = self.suit_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suit_item_list[i] = element.to_alipay_dict()
            if hasattr(self.suit_item_list, 'to_alipay_dict'):
                params['suit_item_list'] = self.suit_item_list.to_alipay_dict()
            else:
                params['suit_item_list'] = self.suit_item_list
        if self.usaged_times:
            if isinstance(self.usaged_times, list):
                for i in range(0, len(self.usaged_times)):
                    element = self.usaged_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.usaged_times[i] = element.to_alipay_dict()
            if hasattr(self.usaged_times, 'to_alipay_dict'):
                params['usaged_times'] = self.usaged_times.to_alipay_dict()
            else:
                params['usaged_times'] = self.usaged_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MEquityUseRule()
        if 'disabled_times' in d:
            o.disabled_times = d['disabled_times']
        if 'min_cost_amount' in d:
            o.min_cost_amount = d['min_cost_amount']
        if 'suit_item_list' in d:
            o.suit_item_list = d['suit_item_list']
        if 'usaged_times' in d:
            o.usaged_times = d['usaged_times']
        return o


