#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstallmentMetaInfo(object):

    def __init__(self):
        self._end_term = None
        self._start_term = None
        self._value = None

    @property
    def end_term(self):
        return self._end_term

    @end_term.setter
    def end_term(self, value):
        self._end_term = value
    @property
    def start_term(self):
        return self._start_term

    @start_term.setter
    def start_term(self, value):
        self._start_term = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_term:
            if hasattr(self.end_term, 'to_alipay_dict'):
                params['end_term'] = self.end_term.to_alipay_dict()
            else:
                params['end_term'] = self.end_term
        if self.start_term:
            if hasattr(self.start_term, 'to_alipay_dict'):
                params['start_term'] = self.start_term.to_alipay_dict()
            else:
                params['start_term'] = self.start_term
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstallmentMetaInfo()
        if 'end_term' in d:
            o.end_term = d['end_term']
        if 'start_term' in d:
            o.start_term = d['start_term']
        if 'value' in d:
            o.value = d['value']
        return o


