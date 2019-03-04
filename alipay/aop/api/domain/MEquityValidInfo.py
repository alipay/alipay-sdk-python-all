#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MEquityValidInfo(object):

    def __init__(self):
        self._delay_minutes = None
        self._effect_type = None
        self._end_date = None
        self._relative_minutes = None
        self._start_date = None
        self._valid_type = None

    @property
    def delay_minutes(self):
        return self._delay_minutes

    @delay_minutes.setter
    def delay_minutes(self, value):
        self._delay_minutes = value
    @property
    def effect_type(self):
        return self._effect_type

    @effect_type.setter
    def effect_type(self, value):
        self._effect_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def relative_minutes(self):
        return self._relative_minutes

    @relative_minutes.setter
    def relative_minutes(self, value):
        self._relative_minutes = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def valid_type(self):
        return self._valid_type

    @valid_type.setter
    def valid_type(self, value):
        self._valid_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delay_minutes:
            if hasattr(self.delay_minutes, 'to_alipay_dict'):
                params['delay_minutes'] = self.delay_minutes.to_alipay_dict()
            else:
                params['delay_minutes'] = self.delay_minutes
        if self.effect_type:
            if hasattr(self.effect_type, 'to_alipay_dict'):
                params['effect_type'] = self.effect_type.to_alipay_dict()
            else:
                params['effect_type'] = self.effect_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.relative_minutes:
            if hasattr(self.relative_minutes, 'to_alipay_dict'):
                params['relative_minutes'] = self.relative_minutes.to_alipay_dict()
            else:
                params['relative_minutes'] = self.relative_minutes
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.valid_type:
            if hasattr(self.valid_type, 'to_alipay_dict'):
                params['valid_type'] = self.valid_type.to_alipay_dict()
            else:
                params['valid_type'] = self.valid_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MEquityValidInfo()
        if 'delay_minutes' in d:
            o.delay_minutes = d['delay_minutes']
        if 'effect_type' in d:
            o.effect_type = d['effect_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'relative_minutes' in d:
            o.relative_minutes = d['relative_minutes']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'valid_type' in d:
            o.valid_type = d['valid_type']
        return o


