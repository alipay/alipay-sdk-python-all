#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CountControlConfig(object):

    def __init__(self):
        self._day_count = None
        self._dimension = None
        self._domain_type = None
        self._life_count = None
        self._month_count = None
        self._week_count = None
        self._year_count = None

    @property
    def day_count(self):
        return self._day_count

    @day_count.setter
    def day_count(self, value):
        self._day_count = value
    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def domain_type(self):
        return self._domain_type

    @domain_type.setter
    def domain_type(self, value):
        self._domain_type = value
    @property
    def life_count(self):
        return self._life_count

    @life_count.setter
    def life_count(self, value):
        self._life_count = value
    @property
    def month_count(self):
        return self._month_count

    @month_count.setter
    def month_count(self, value):
        self._month_count = value
    @property
    def week_count(self):
        return self._week_count

    @week_count.setter
    def week_count(self, value):
        self._week_count = value
    @property
    def year_count(self):
        return self._year_count

    @year_count.setter
    def year_count(self, value):
        self._year_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.day_count:
            if hasattr(self.day_count, 'to_alipay_dict'):
                params['day_count'] = self.day_count.to_alipay_dict()
            else:
                params['day_count'] = self.day_count
        if self.dimension:
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
        if self.domain_type:
            if hasattr(self.domain_type, 'to_alipay_dict'):
                params['domain_type'] = self.domain_type.to_alipay_dict()
            else:
                params['domain_type'] = self.domain_type
        if self.life_count:
            if hasattr(self.life_count, 'to_alipay_dict'):
                params['life_count'] = self.life_count.to_alipay_dict()
            else:
                params['life_count'] = self.life_count
        if self.month_count:
            if hasattr(self.month_count, 'to_alipay_dict'):
                params['month_count'] = self.month_count.to_alipay_dict()
            else:
                params['month_count'] = self.month_count
        if self.week_count:
            if hasattr(self.week_count, 'to_alipay_dict'):
                params['week_count'] = self.week_count.to_alipay_dict()
            else:
                params['week_count'] = self.week_count
        if self.year_count:
            if hasattr(self.year_count, 'to_alipay_dict'):
                params['year_count'] = self.year_count.to_alipay_dict()
            else:
                params['year_count'] = self.year_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CountControlConfig()
        if 'day_count' in d:
            o.day_count = d['day_count']
        if 'dimension' in d:
            o.dimension = d['dimension']
        if 'domain_type' in d:
            o.domain_type = d['domain_type']
        if 'life_count' in d:
            o.life_count = d['life_count']
        if 'month_count' in d:
            o.month_count = d['month_count']
        if 'week_count' in d:
            o.week_count = d['week_count']
        if 'year_count' in d:
            o.year_count = d['year_count']
        return o


