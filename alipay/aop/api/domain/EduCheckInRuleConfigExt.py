#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduCheckInRuleConfigExt(object):

    def __init__(self):
        self._end_minutes = None
        self._end_type = None
        self._start_minutes = None
        self._start_type = None

    @property
    def end_minutes(self):
        return self._end_minutes

    @end_minutes.setter
    def end_minutes(self, value):
        self._end_minutes = value
    @property
    def end_type(self):
        return self._end_type

    @end_type.setter
    def end_type(self, value):
        self._end_type = value
    @property
    def start_minutes(self):
        return self._start_minutes

    @start_minutes.setter
    def start_minutes(self, value):
        self._start_minutes = value
    @property
    def start_type(self):
        return self._start_type

    @start_type.setter
    def start_type(self, value):
        self._start_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_minutes:
            if hasattr(self.end_minutes, 'to_alipay_dict'):
                params['end_minutes'] = self.end_minutes.to_alipay_dict()
            else:
                params['end_minutes'] = self.end_minutes
        if self.end_type:
            if hasattr(self.end_type, 'to_alipay_dict'):
                params['end_type'] = self.end_type.to_alipay_dict()
            else:
                params['end_type'] = self.end_type
        if self.start_minutes:
            if hasattr(self.start_minutes, 'to_alipay_dict'):
                params['start_minutes'] = self.start_minutes.to_alipay_dict()
            else:
                params['start_minutes'] = self.start_minutes
        if self.start_type:
            if hasattr(self.start_type, 'to_alipay_dict'):
                params['start_type'] = self.start_type.to_alipay_dict()
            else:
                params['start_type'] = self.start_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduCheckInRuleConfigExt()
        if 'end_minutes' in d:
            o.end_minutes = d['end_minutes']
        if 'end_type' in d:
            o.end_type = d['end_type']
        if 'start_minutes' in d:
            o.start_minutes = d['start_minutes']
        if 'start_type' in d:
            o.start_type = d['start_type']
        return o


