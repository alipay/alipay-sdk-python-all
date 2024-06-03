#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SellRankMonthConfig(object):

    def __init__(self):
        self._month = None
        self._text = None

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellRankMonthConfig()
        if 'month' in d:
            o.month = d['month']
        if 'text' in d:
            o.text = d['text']
        return o


