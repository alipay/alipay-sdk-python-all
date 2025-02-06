#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataHqtestCreateModel(object):

    def __init__(self):
        self._bool = None
        self._bool_arr = None
        self._date = None
        self._date_arr = None
        self._test = None
        self._total = None

    @property
    def bool(self):
        return self._bool

    @bool.setter
    def bool(self, value):
        self._bool = value
    @property
    def bool_arr(self):
        return self._bool_arr

    @bool_arr.setter
    def bool_arr(self, value):
        if isinstance(value, list):
            self._bool_arr = list()
            for i in value:
                self._bool_arr.append(i)
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def date_arr(self):
        return self._date_arr

    @date_arr.setter
    def date_arr(self, value):
        if isinstance(value, list):
            self._date_arr = list()
            for i in value:
                self._date_arr.append(i)
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.bool:
            if hasattr(self.bool, 'to_alipay_dict'):
                params['bool'] = self.bool.to_alipay_dict()
            else:
                params['bool'] = self.bool
        if self.bool_arr:
            if isinstance(self.bool_arr, list):
                for i in range(0, len(self.bool_arr)):
                    element = self.bool_arr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bool_arr[i] = element.to_alipay_dict()
            if hasattr(self.bool_arr, 'to_alipay_dict'):
                params['bool_arr'] = self.bool_arr.to_alipay_dict()
            else:
                params['bool_arr'] = self.bool_arr
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.date_arr:
            if isinstance(self.date_arr, list):
                for i in range(0, len(self.date_arr)):
                    element = self.date_arr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_arr[i] = element.to_alipay_dict()
            if hasattr(self.date_arr, 'to_alipay_dict'):
                params['date_arr'] = self.date_arr.to_alipay_dict()
            else:
                params['date_arr'] = self.date_arr
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataHqtestCreateModel()
        if 'bool' in d:
            o.bool = d['bool']
        if 'bool_arr' in d:
            o.bool_arr = d['bool_arr']
        if 'date' in d:
            o.date = d['date']
        if 'date_arr' in d:
            o.date_arr = d['date_arr']
        if 'test' in d:
            o.test = d['test']
        if 'total' in d:
            o.total = d['total']
        return o


