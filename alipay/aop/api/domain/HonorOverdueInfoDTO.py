#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorOverdueInfoDTO(object):

    def __init__(self):
        self._overdue_amount = None
        self._overdue_days = None
        self._overdue_order = None
        self._overdue_penalty = None

    @property
    def overdue_amount(self):
        return self._overdue_amount

    @overdue_amount.setter
    def overdue_amount(self, value):
        self._overdue_amount = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
    @property
    def overdue_order(self):
        return self._overdue_order

    @overdue_order.setter
    def overdue_order(self, value):
        self._overdue_order = value
    @property
    def overdue_penalty(self):
        return self._overdue_penalty

    @overdue_penalty.setter
    def overdue_penalty(self, value):
        self._overdue_penalty = value


    def to_alipay_dict(self):
        params = dict()
        if self.overdue_amount:
            if hasattr(self.overdue_amount, 'to_alipay_dict'):
                params['overdue_amount'] = self.overdue_amount.to_alipay_dict()
            else:
                params['overdue_amount'] = self.overdue_amount
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
        if self.overdue_order:
            if hasattr(self.overdue_order, 'to_alipay_dict'):
                params['overdue_order'] = self.overdue_order.to_alipay_dict()
            else:
                params['overdue_order'] = self.overdue_order
        if self.overdue_penalty:
            if hasattr(self.overdue_penalty, 'to_alipay_dict'):
                params['overdue_penalty'] = self.overdue_penalty.to_alipay_dict()
            else:
                params['overdue_penalty'] = self.overdue_penalty
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorOverdueInfoDTO()
        if 'overdue_amount' in d:
            o.overdue_amount = d['overdue_amount']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'overdue_order' in d:
            o.overdue_order = d['overdue_order']
        if 'overdue_penalty' in d:
            o.overdue_penalty = d['overdue_penalty']
        return o


