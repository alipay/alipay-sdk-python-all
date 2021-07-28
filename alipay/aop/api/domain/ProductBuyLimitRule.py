#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductBuyLimitRule(object):

    def __init__(self):
        self._buy_time_limit = None
        self._can_buy_limit_type = None
        self._can_buy_max_count = None
        self._can_buy_min_count = None
        self._category_choose_max_count = None
        self._category_choose_min_count = None
        self._daily_end_time = None
        self._daily_start_time = None

    @property
    def buy_time_limit(self):
        return self._buy_time_limit

    @buy_time_limit.setter
    def buy_time_limit(self, value):
        if isinstance(value, list):
            self._buy_time_limit = list()
            for i in value:
                self._buy_time_limit.append(i)
    @property
    def can_buy_limit_type(self):
        return self._can_buy_limit_type

    @can_buy_limit_type.setter
    def can_buy_limit_type(self, value):
        self._can_buy_limit_type = value
    @property
    def can_buy_max_count(self):
        return self._can_buy_max_count

    @can_buy_max_count.setter
    def can_buy_max_count(self, value):
        self._can_buy_max_count = value
    @property
    def can_buy_min_count(self):
        return self._can_buy_min_count

    @can_buy_min_count.setter
    def can_buy_min_count(self, value):
        self._can_buy_min_count = value
    @property
    def category_choose_max_count(self):
        return self._category_choose_max_count

    @category_choose_max_count.setter
    def category_choose_max_count(self, value):
        self._category_choose_max_count = value
    @property
    def category_choose_min_count(self):
        return self._category_choose_min_count

    @category_choose_min_count.setter
    def category_choose_min_count(self, value):
        self._category_choose_min_count = value
    @property
    def daily_end_time(self):
        return self._daily_end_time

    @daily_end_time.setter
    def daily_end_time(self, value):
        self._daily_end_time = value
    @property
    def daily_start_time(self):
        return self._daily_start_time

    @daily_start_time.setter
    def daily_start_time(self, value):
        self._daily_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.buy_time_limit:
            if isinstance(self.buy_time_limit, list):
                for i in range(0, len(self.buy_time_limit)):
                    element = self.buy_time_limit[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.buy_time_limit[i] = element.to_alipay_dict()
            if hasattr(self.buy_time_limit, 'to_alipay_dict'):
                params['buy_time_limit'] = self.buy_time_limit.to_alipay_dict()
            else:
                params['buy_time_limit'] = self.buy_time_limit
        if self.can_buy_limit_type:
            if hasattr(self.can_buy_limit_type, 'to_alipay_dict'):
                params['can_buy_limit_type'] = self.can_buy_limit_type.to_alipay_dict()
            else:
                params['can_buy_limit_type'] = self.can_buy_limit_type
        if self.can_buy_max_count:
            if hasattr(self.can_buy_max_count, 'to_alipay_dict'):
                params['can_buy_max_count'] = self.can_buy_max_count.to_alipay_dict()
            else:
                params['can_buy_max_count'] = self.can_buy_max_count
        if self.can_buy_min_count:
            if hasattr(self.can_buy_min_count, 'to_alipay_dict'):
                params['can_buy_min_count'] = self.can_buy_min_count.to_alipay_dict()
            else:
                params['can_buy_min_count'] = self.can_buy_min_count
        if self.category_choose_max_count:
            if hasattr(self.category_choose_max_count, 'to_alipay_dict'):
                params['category_choose_max_count'] = self.category_choose_max_count.to_alipay_dict()
            else:
                params['category_choose_max_count'] = self.category_choose_max_count
        if self.category_choose_min_count:
            if hasattr(self.category_choose_min_count, 'to_alipay_dict'):
                params['category_choose_min_count'] = self.category_choose_min_count.to_alipay_dict()
            else:
                params['category_choose_min_count'] = self.category_choose_min_count
        if self.daily_end_time:
            if hasattr(self.daily_end_time, 'to_alipay_dict'):
                params['daily_end_time'] = self.daily_end_time.to_alipay_dict()
            else:
                params['daily_end_time'] = self.daily_end_time
        if self.daily_start_time:
            if hasattr(self.daily_start_time, 'to_alipay_dict'):
                params['daily_start_time'] = self.daily_start_time.to_alipay_dict()
            else:
                params['daily_start_time'] = self.daily_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductBuyLimitRule()
        if 'buy_time_limit' in d:
            o.buy_time_limit = d['buy_time_limit']
        if 'can_buy_limit_type' in d:
            o.can_buy_limit_type = d['can_buy_limit_type']
        if 'can_buy_max_count' in d:
            o.can_buy_max_count = d['can_buy_max_count']
        if 'can_buy_min_count' in d:
            o.can_buy_min_count = d['can_buy_min_count']
        if 'category_choose_max_count' in d:
            o.category_choose_max_count = d['category_choose_max_count']
        if 'category_choose_min_count' in d:
            o.category_choose_min_count = d['category_choose_min_count']
        if 'daily_end_time' in d:
            o.daily_end_time = d['daily_end_time']
        if 'daily_start_time' in d:
            o.daily_start_time = d['daily_start_time']
        return o


