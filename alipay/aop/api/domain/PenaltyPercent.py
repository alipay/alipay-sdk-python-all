#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PenaltyPercent(object):

    def __init__(self):
        self._nights = None
        self._percent = None

    @property
    def nights(self):
        return self._nights

    @nights.setter
    def nights(self, value):
        self._nights = value
    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        self._percent = value


    def to_alipay_dict(self):
        params = dict()
        if self.nights:
            if hasattr(self.nights, 'to_alipay_dict'):
                params['nights'] = self.nights.to_alipay_dict()
            else:
                params['nights'] = self.nights
        if self.percent:
            if hasattr(self.percent, 'to_alipay_dict'):
                params['percent'] = self.percent.to_alipay_dict()
            else:
                params['percent'] = self.percent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PenaltyPercent()
        if 'nights' in d:
            o.nights = d['nights']
        if 'percent' in d:
            o.percent = d['percent']
        return o


