#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VcpCalcCondition(object):

    def __init__(self):
        self._condition_item_ids = None
        self._from_amount = None
        self._from_time = None
        self._item_ids = None
        self._threshold_amount_type = None
        self._threshold_count = None
        self._to_amount = None
        self._to_time = None

    @property
    def condition_item_ids(self):
        return self._condition_item_ids

    @condition_item_ids.setter
    def condition_item_ids(self, value):
        if isinstance(value, list):
            self._condition_item_ids = list()
            for i in value:
                self._condition_item_ids.append(i)
    @property
    def from_amount(self):
        return self._from_amount

    @from_amount.setter
    def from_amount(self, value):
        self._from_amount = value
    @property
    def from_time(self):
        return self._from_time

    @from_time.setter
    def from_time(self, value):
        self._from_time = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def threshold_amount_type(self):
        return self._threshold_amount_type

    @threshold_amount_type.setter
    def threshold_amount_type(self, value):
        self._threshold_amount_type = value
    @property
    def threshold_count(self):
        return self._threshold_count

    @threshold_count.setter
    def threshold_count(self, value):
        self._threshold_count = value
    @property
    def to_amount(self):
        return self._to_amount

    @to_amount.setter
    def to_amount(self, value):
        self._to_amount = value
    @property
    def to_time(self):
        return self._to_time

    @to_time.setter
    def to_time(self, value):
        self._to_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_item_ids:
            if isinstance(self.condition_item_ids, list):
                for i in range(0, len(self.condition_item_ids)):
                    element = self.condition_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.condition_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.condition_item_ids, 'to_alipay_dict'):
                params['condition_item_ids'] = self.condition_item_ids.to_alipay_dict()
            else:
                params['condition_item_ids'] = self.condition_item_ids
        if self.from_amount:
            if hasattr(self.from_amount, 'to_alipay_dict'):
                params['from_amount'] = self.from_amount.to_alipay_dict()
            else:
                params['from_amount'] = self.from_amount
        if self.from_time:
            if hasattr(self.from_time, 'to_alipay_dict'):
                params['from_time'] = self.from_time.to_alipay_dict()
            else:
                params['from_time'] = self.from_time
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.threshold_amount_type:
            if hasattr(self.threshold_amount_type, 'to_alipay_dict'):
                params['threshold_amount_type'] = self.threshold_amount_type.to_alipay_dict()
            else:
                params['threshold_amount_type'] = self.threshold_amount_type
        if self.threshold_count:
            if hasattr(self.threshold_count, 'to_alipay_dict'):
                params['threshold_count'] = self.threshold_count.to_alipay_dict()
            else:
                params['threshold_count'] = self.threshold_count
        if self.to_amount:
            if hasattr(self.to_amount, 'to_alipay_dict'):
                params['to_amount'] = self.to_amount.to_alipay_dict()
            else:
                params['to_amount'] = self.to_amount
        if self.to_time:
            if hasattr(self.to_time, 'to_alipay_dict'):
                params['to_time'] = self.to_time.to_alipay_dict()
            else:
                params['to_time'] = self.to_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpCalcCondition()
        if 'condition_item_ids' in d:
            o.condition_item_ids = d['condition_item_ids']
        if 'from_amount' in d:
            o.from_amount = d['from_amount']
        if 'from_time' in d:
            o.from_time = d['from_time']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'threshold_amount_type' in d:
            o.threshold_amount_type = d['threshold_amount_type']
        if 'threshold_count' in d:
            o.threshold_count = d['threshold_count']
        if 'to_amount' in d:
            o.to_amount = d['to_amount']
        if 'to_time' in d:
            o.to_time = d['to_time']
        return o


