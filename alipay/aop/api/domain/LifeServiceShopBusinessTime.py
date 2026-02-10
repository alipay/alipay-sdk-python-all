#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceShopBusinessTime(object):

    def __init__(self):
        self._always_open = None
        self._close_time = None
        self._open_time = None
        self._week_days = None

    @property
    def always_open(self):
        return self._always_open

    @always_open.setter
    def always_open(self, value):
        self._always_open = value
    @property
    def close_time(self):
        return self._close_time

    @close_time.setter
    def close_time(self, value):
        self._close_time = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def week_days(self):
        return self._week_days

    @week_days.setter
    def week_days(self, value):
        self._week_days = value


    def to_alipay_dict(self):
        params = dict()
        if self.always_open:
            if hasattr(self.always_open, 'to_alipay_dict'):
                params['always_open'] = self.always_open.to_alipay_dict()
            else:
                params['always_open'] = self.always_open
        if self.close_time:
            if hasattr(self.close_time, 'to_alipay_dict'):
                params['close_time'] = self.close_time.to_alipay_dict()
            else:
                params['close_time'] = self.close_time
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.week_days:
            if hasattr(self.week_days, 'to_alipay_dict'):
                params['week_days'] = self.week_days.to_alipay_dict()
            else:
                params['week_days'] = self.week_days
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceShopBusinessTime()
        if 'always_open' in d:
            o.always_open = d['always_open']
        if 'close_time' in d:
            o.close_time = d['close_time']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'week_days' in d:
            o.week_days = d['week_days']
        return o


