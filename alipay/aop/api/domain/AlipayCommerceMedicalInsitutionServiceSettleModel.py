#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsitutionServiceSettleModel(object):

    def __init__(self):
        self._end_date = None
        self._indicator_type = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def indicator_type(self):
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, value):
        self._indicator_type = value
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
        if self.indicator_type:
            if hasattr(self.indicator_type, 'to_alipay_dict'):
                params['indicator_type'] = self.indicator_type.to_alipay_dict()
            else:
                params['indicator_type'] = self.indicator_type
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
        o = AlipayCommerceMedicalInsitutionServiceSettleModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'indicator_type' in d:
            o.indicator_type = d['indicator_type']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


