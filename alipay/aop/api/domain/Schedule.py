#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Schedule(object):

    def __init__(self):
        self._open = None
        self._param_id = None
        self._param_name = None
        self._period = None
        self._period_crond_expr = None
        self._type = None

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def param_id(self):
        return self._param_id

    @param_id.setter
    def param_id(self, value):
        self._param_id = value
    @property
    def param_name(self):
        return self._param_name

    @param_name.setter
    def param_name(self, value):
        self._param_name = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_crond_expr(self):
        return self._period_crond_expr

    @period_crond_expr.setter
    def period_crond_expr(self, value):
        self._period_crond_expr = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.open:
            if hasattr(self.open, 'to_alipay_dict'):
                params['open'] = self.open.to_alipay_dict()
            else:
                params['open'] = self.open
        if self.param_id:
            if hasattr(self.param_id, 'to_alipay_dict'):
                params['param_id'] = self.param_id.to_alipay_dict()
            else:
                params['param_id'] = self.param_id
        if self.param_name:
            if hasattr(self.param_name, 'to_alipay_dict'):
                params['param_name'] = self.param_name.to_alipay_dict()
            else:
                params['param_name'] = self.param_name
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_crond_expr:
            if hasattr(self.period_crond_expr, 'to_alipay_dict'):
                params['period_crond_expr'] = self.period_crond_expr.to_alipay_dict()
            else:
                params['period_crond_expr'] = self.period_crond_expr
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Schedule()
        if 'open' in d:
            o.open = d['open']
        if 'param_id' in d:
            o.param_id = d['param_id']
        if 'param_name' in d:
            o.param_name = d['param_name']
        if 'period' in d:
            o.period = d['period']
        if 'period_crond_expr' in d:
            o.period_crond_expr = d['period_crond_expr']
        if 'type' in d:
            o.type = d['type']
        return o


