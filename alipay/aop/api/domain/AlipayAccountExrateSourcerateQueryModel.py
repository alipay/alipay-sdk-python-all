#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountExrateSourcerateQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._generate_date = None
        self._is_exception = None
        self._rate_source_code = None
        self._size = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def generate_date(self):
        return self._generate_date

    @generate_date.setter
    def generate_date(self, value):
        self._generate_date = value
    @property
    def is_exception(self):
        return self._is_exception

    @is_exception.setter
    def is_exception(self, value):
        self._is_exception = value
    @property
    def rate_source_code(self):
        return self._rate_source_code

    @rate_source_code.setter
    def rate_source_code(self, value):
        self._rate_source_code = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.generate_date:
            if hasattr(self.generate_date, 'to_alipay_dict'):
                params['generate_date'] = self.generate_date.to_alipay_dict()
            else:
                params['generate_date'] = self.generate_date
        if self.is_exception:
            if hasattr(self.is_exception, 'to_alipay_dict'):
                params['is_exception'] = self.is_exception.to_alipay_dict()
            else:
                params['is_exception'] = self.is_exception
        if self.rate_source_code:
            if hasattr(self.rate_source_code, 'to_alipay_dict'):
                params['rate_source_code'] = self.rate_source_code.to_alipay_dict()
            else:
                params['rate_source_code'] = self.rate_source_code
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExrateSourcerateQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'generate_date' in d:
            o.generate_date = d['generate_date']
        if 'is_exception' in d:
            o.is_exception = d['is_exception']
        if 'rate_source_code' in d:
            o.rate_source_code = d['rate_source_code']
        if 'size' in d:
            o.size = d['size']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


