#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemCalendarPriceVO(object):

    def __init__(self):
        self._end_date = None
        self._exclude_dates = None
        self._original_price = None
        self._sale_price = None
        self._start_date = None
        self._status = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def exclude_dates(self):
        return self._exclude_dates

    @exclude_dates.setter
    def exclude_dates(self, value):
        if isinstance(value, list):
            self._exclude_dates = list()
            for i in value:
                self._exclude_dates.append(i)
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.exclude_dates:
            if isinstance(self.exclude_dates, list):
                for i in range(0, len(self.exclude_dates)):
                    element = self.exclude_dates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exclude_dates[i] = element.to_alipay_dict()
            if hasattr(self.exclude_dates, 'to_alipay_dict'):
                params['exclude_dates'] = self.exclude_dates.to_alipay_dict()
            else:
                params['exclude_dates'] = self.exclude_dates
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemCalendarPriceVO()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'exclude_dates' in d:
            o.exclude_dates = d['exclude_dates']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'status' in d:
            o.status = d['status']
        return o


