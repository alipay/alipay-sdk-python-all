#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RankSaleTrendResult(object):

    def __init__(self):
        self._city_name = None
        self._end_date = None
        self._last_rank_value = None
        self._month = None
        self._rank = None
        self._rank_value = None
        self._start_date = None

    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def last_rank_value(self):
        return self._last_rank_value

    @last_rank_value.setter
    def last_rank_value(self, value):
        self._last_rank_value = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def rank_value(self):
        return self._rank_value

    @rank_value.setter
    def rank_value(self, value):
        self._rank_value = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.last_rank_value:
            if hasattr(self.last_rank_value, 'to_alipay_dict'):
                params['last_rank_value'] = self.last_rank_value.to_alipay_dict()
            else:
                params['last_rank_value'] = self.last_rank_value
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.rank_value:
            if hasattr(self.rank_value, 'to_alipay_dict'):
                params['rank_value'] = self.rank_value.to_alipay_dict()
            else:
                params['rank_value'] = self.rank_value
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RankSaleTrendResult()
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'last_rank_value' in d:
            o.last_rank_value = d['last_rank_value']
        if 'month' in d:
            o.month = d['month']
        if 'rank' in d:
            o.rank = d['rank']
        if 'rank_value' in d:
            o.rank_value = d['rank_value']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


