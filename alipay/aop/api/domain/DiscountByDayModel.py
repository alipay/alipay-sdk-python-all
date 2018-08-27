#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountByDayModel(object):

    def __init__(self):
        self._begin_day = None
        self._discount = None
        self._end_day = None

    @property
    def begin_day(self):
        return self._begin_day

    @begin_day.setter
    def begin_day(self, value):
        self._begin_day = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def end_day(self):
        return self._end_day

    @end_day.setter
    def end_day(self, value):
        self._end_day = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_day:
            if hasattr(self.begin_day, 'to_alipay_dict'):
                params['begin_day'] = self.begin_day.to_alipay_dict()
            else:
                params['begin_day'] = self.begin_day
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.end_day:
            if hasattr(self.end_day, 'to_alipay_dict'):
                params['end_day'] = self.end_day.to_alipay_dict()
            else:
                params['end_day'] = self.end_day
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountByDayModel()
        if 'begin_day' in d:
            o.begin_day = d['begin_day']
        if 'discount' in d:
            o.discount = d['discount']
        if 'end_day' in d:
            o.end_day = d['end_day']
        return o


