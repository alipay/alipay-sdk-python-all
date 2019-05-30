#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossOrderDiagnosisGetModel(object):

    def __init__(self):
        self._code = None
        self._end_time = None
        self._find_operator = None
        self._order_no = None
        self._out_order_no = None
        self._source = None
        self._start_time = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def find_operator(self):
        return self._find_operator

    @find_operator.setter
    def find_operator(self, value):
        self._find_operator = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.find_operator:
            if hasattr(self.find_operator, 'to_alipay_dict'):
                params['find_operator'] = self.find_operator.to_alipay_dict()
            else:
                params['find_operator'] = self.find_operator
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayBossOrderDiagnosisGetModel()
        if 'code' in d:
            o.code = d['code']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'find_operator' in d:
            o.find_operator = d['find_operator']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'source' in d:
            o.source = d['source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


