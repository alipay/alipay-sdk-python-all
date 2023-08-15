#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommercializationCertificateInfo(object):

    def __init__(self):
        self._code = None
        self._total_times = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def total_times(self):
        return self._total_times

    @total_times.setter
    def total_times(self, value):
        self._total_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.total_times:
            if hasattr(self.total_times, 'to_alipay_dict'):
                params['total_times'] = self.total_times.to_alipay_dict()
            else:
                params['total_times'] = self.total_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommercializationCertificateInfo()
        if 'code' in d:
            o.code = d['code']
        if 'total_times' in d:
            o.total_times = d['total_times']
        return o


