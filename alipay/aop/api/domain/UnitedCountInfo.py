#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UnitedCountInfo(object):

    def __init__(self):
        self._max_day_count = None
        self._max_life_count = None
        self._max_month_count = None
        self._max_week_count = None
        self._remain_day_count = None
        self._remain_life_count = None
        self._remain_month_count = None
        self._remain_week_count = None

    @property
    def max_day_count(self):
        return self._max_day_count

    @max_day_count.setter
    def max_day_count(self, value):
        self._max_day_count = value
    @property
    def max_life_count(self):
        return self._max_life_count

    @max_life_count.setter
    def max_life_count(self, value):
        self._max_life_count = value
    @property
    def max_month_count(self):
        return self._max_month_count

    @max_month_count.setter
    def max_month_count(self, value):
        self._max_month_count = value
    @property
    def max_week_count(self):
        return self._max_week_count

    @max_week_count.setter
    def max_week_count(self, value):
        self._max_week_count = value
    @property
    def remain_day_count(self):
        return self._remain_day_count

    @remain_day_count.setter
    def remain_day_count(self, value):
        self._remain_day_count = value
    @property
    def remain_life_count(self):
        return self._remain_life_count

    @remain_life_count.setter
    def remain_life_count(self, value):
        self._remain_life_count = value
    @property
    def remain_month_count(self):
        return self._remain_month_count

    @remain_month_count.setter
    def remain_month_count(self, value):
        self._remain_month_count = value
    @property
    def remain_week_count(self):
        return self._remain_week_count

    @remain_week_count.setter
    def remain_week_count(self, value):
        self._remain_week_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_day_count:
            if hasattr(self.max_day_count, 'to_alipay_dict'):
                params['max_day_count'] = self.max_day_count.to_alipay_dict()
            else:
                params['max_day_count'] = self.max_day_count
        if self.max_life_count:
            if hasattr(self.max_life_count, 'to_alipay_dict'):
                params['max_life_count'] = self.max_life_count.to_alipay_dict()
            else:
                params['max_life_count'] = self.max_life_count
        if self.max_month_count:
            if hasattr(self.max_month_count, 'to_alipay_dict'):
                params['max_month_count'] = self.max_month_count.to_alipay_dict()
            else:
                params['max_month_count'] = self.max_month_count
        if self.max_week_count:
            if hasattr(self.max_week_count, 'to_alipay_dict'):
                params['max_week_count'] = self.max_week_count.to_alipay_dict()
            else:
                params['max_week_count'] = self.max_week_count
        if self.remain_day_count:
            if hasattr(self.remain_day_count, 'to_alipay_dict'):
                params['remain_day_count'] = self.remain_day_count.to_alipay_dict()
            else:
                params['remain_day_count'] = self.remain_day_count
        if self.remain_life_count:
            if hasattr(self.remain_life_count, 'to_alipay_dict'):
                params['remain_life_count'] = self.remain_life_count.to_alipay_dict()
            else:
                params['remain_life_count'] = self.remain_life_count
        if self.remain_month_count:
            if hasattr(self.remain_month_count, 'to_alipay_dict'):
                params['remain_month_count'] = self.remain_month_count.to_alipay_dict()
            else:
                params['remain_month_count'] = self.remain_month_count
        if self.remain_week_count:
            if hasattr(self.remain_week_count, 'to_alipay_dict'):
                params['remain_week_count'] = self.remain_week_count.to_alipay_dict()
            else:
                params['remain_week_count'] = self.remain_week_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UnitedCountInfo()
        if 'max_day_count' in d:
            o.max_day_count = d['max_day_count']
        if 'max_life_count' in d:
            o.max_life_count = d['max_life_count']
        if 'max_month_count' in d:
            o.max_month_count = d['max_month_count']
        if 'max_week_count' in d:
            o.max_week_count = d['max_week_count']
        if 'remain_day_count' in d:
            o.remain_day_count = d['remain_day_count']
        if 'remain_life_count' in d:
            o.remain_life_count = d['remain_life_count']
        if 'remain_month_count' in d:
            o.remain_month_count = d['remain_month_count']
        if 'remain_week_count' in d:
            o.remain_week_count = d['remain_week_count']
        return o


