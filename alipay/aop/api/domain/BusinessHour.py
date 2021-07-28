#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessHourItem import BusinessHourItem


class BusinessHour(object):

    def __init__(self):
        self._end_date = None
        self._hour_items = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def hour_items(self):
        return self._hour_items

    @hour_items.setter
    def hour_items(self, value):
        if isinstance(value, list):
            self._hour_items = list()
            for i in value:
                if isinstance(i, BusinessHourItem):
                    self._hour_items.append(i)
                else:
                    self._hour_items.append(BusinessHourItem.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.hour_items:
            if isinstance(self.hour_items, list):
                for i in range(0, len(self.hour_items)):
                    element = self.hour_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hour_items[i] = element.to_alipay_dict()
            if hasattr(self.hour_items, 'to_alipay_dict'):
                params['hour_items'] = self.hour_items.to_alipay_dict()
            else:
                params['hour_items'] = self.hour_items
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessHour()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'hour_items' in d:
            o.hour_items = d['hour_items']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


