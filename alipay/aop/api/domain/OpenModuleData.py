#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenPayResultSummary import OpenPayResultSummary


class OpenModuleData(object):

    def __init__(self):
        self._red_code = None
        self._summary = None

    @property
    def red_code(self):
        return self._red_code

    @red_code.setter
    def red_code(self, value):
        self._red_code = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, OpenPayResultSummary):
            self._summary = value
        else:
            self._summary = OpenPayResultSummary.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.red_code:
            if hasattr(self.red_code, 'to_alipay_dict'):
                params['red_code'] = self.red_code.to_alipay_dict()
            else:
                params['red_code'] = self.red_code
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenModuleData()
        if 'red_code' in d:
            o.red_code = d['red_code']
        if 'summary' in d:
            o.summary = d['summary']
        return o


