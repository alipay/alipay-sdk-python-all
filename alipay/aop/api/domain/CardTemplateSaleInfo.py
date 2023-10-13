#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardTemplateSaleInfo(object):

    def __init__(self):
        self._salable_end_time = None
        self._salable_start_time = None

    @property
    def salable_end_time(self):
        return self._salable_end_time

    @salable_end_time.setter
    def salable_end_time(self, value):
        self._salable_end_time = value
    @property
    def salable_start_time(self):
        return self._salable_start_time

    @salable_start_time.setter
    def salable_start_time(self, value):
        self._salable_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.salable_end_time:
            if hasattr(self.salable_end_time, 'to_alipay_dict'):
                params['salable_end_time'] = self.salable_end_time.to_alipay_dict()
            else:
                params['salable_end_time'] = self.salable_end_time
        if self.salable_start_time:
            if hasattr(self.salable_start_time, 'to_alipay_dict'):
                params['salable_start_time'] = self.salable_start_time.to_alipay_dict()
            else:
                params['salable_start_time'] = self.salable_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardTemplateSaleInfo()
        if 'salable_end_time' in d:
            o.salable_end_time = d['salable_end_time']
        if 'salable_start_time' in d:
            o.salable_start_time = d['salable_start_time']
        return o


