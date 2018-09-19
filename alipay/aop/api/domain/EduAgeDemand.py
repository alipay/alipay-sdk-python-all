#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduAgeDemand(object):

    def __init__(self):
        self._age_end = None
        self._age_start = None

    @property
    def age_end(self):
        return self._age_end

    @age_end.setter
    def age_end(self, value):
        self._age_end = value
    @property
    def age_start(self):
        return self._age_start

    @age_start.setter
    def age_start(self, value):
        self._age_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_end:
            if hasattr(self.age_end, 'to_alipay_dict'):
                params['age_end'] = self.age_end.to_alipay_dict()
            else:
                params['age_end'] = self.age_end
        if self.age_start:
            if hasattr(self.age_start, 'to_alipay_dict'):
                params['age_start'] = self.age_start.to_alipay_dict()
            else:
                params['age_start'] = self.age_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduAgeDemand()
        if 'age_end' in d:
            o.age_end = d['age_end']
        if 'age_start' in d:
            o.age_start = d['age_start']
        return o


