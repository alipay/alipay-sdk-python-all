#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SellRankWeekConfig(object):

    def __init__(self):
        self._text = None
        self._week = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def week(self):
        return self._week

    @week.setter
    def week(self, value):
        self._week = value


    def to_alipay_dict(self):
        params = dict()
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        if self.week:
            if hasattr(self.week, 'to_alipay_dict'):
                params['week'] = self.week.to_alipay_dict()
            else:
                params['week'] = self.week
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellRankWeekConfig()
        if 'text' in d:
            o.text = d['text']
        if 'week' in d:
            o.week = d['week']
        return o


