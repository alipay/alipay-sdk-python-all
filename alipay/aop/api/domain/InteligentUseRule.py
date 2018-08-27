#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteligentForbiddenTime import InteligentForbiddenTime
from alipay.aop.api.domain.InteligentUseTime import InteligentUseTime
from alipay.aop.api.domain.InteligentDataCondition import InteligentDataCondition


class InteligentUseRule(object):

    def __init__(self):
        self._inteligent_forbidden_time = None
        self._inteligent_use_times = None
        self._limit_rule = None
        self._min_consume = None
        self._min_consume_condition = None
        self._pay_redirect_url = None
        self._suit_shops = None

    @property
    def inteligent_forbidden_time(self):
        return self._inteligent_forbidden_time

    @inteligent_forbidden_time.setter
    def inteligent_forbidden_time(self, value):
        if isinstance(value, InteligentForbiddenTime):
            self._inteligent_forbidden_time = value
        else:
            self._inteligent_forbidden_time = InteligentForbiddenTime.from_alipay_dict(value)
    @property
    def inteligent_use_times(self):
        return self._inteligent_use_times

    @inteligent_use_times.setter
    def inteligent_use_times(self, value):
        if isinstance(value, list):
            self._inteligent_use_times = list()
            for i in value:
                if isinstance(i, InteligentUseTime):
                    self._inteligent_use_times.append(i)
                else:
                    self._inteligent_use_times.append(InteligentUseTime.from_alipay_dict(i))
    @property
    def limit_rule(self):
        return self._limit_rule

    @limit_rule.setter
    def limit_rule(self, value):
        self._limit_rule = value
    @property
    def min_consume(self):
        return self._min_consume

    @min_consume.setter
    def min_consume(self, value):
        self._min_consume = value
    @property
    def min_consume_condition(self):
        return self._min_consume_condition

    @min_consume_condition.setter
    def min_consume_condition(self, value):
        if isinstance(value, InteligentDataCondition):
            self._min_consume_condition = value
        else:
            self._min_consume_condition = InteligentDataCondition.from_alipay_dict(value)
    @property
    def pay_redirect_url(self):
        return self._pay_redirect_url

    @pay_redirect_url.setter
    def pay_redirect_url(self, value):
        self._pay_redirect_url = value
    @property
    def suit_shops(self):
        return self._suit_shops

    @suit_shops.setter
    def suit_shops(self, value):
        if isinstance(value, list):
            self._suit_shops = list()
            for i in value:
                self._suit_shops.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.inteligent_forbidden_time:
            if hasattr(self.inteligent_forbidden_time, 'to_alipay_dict'):
                params['inteligent_forbidden_time'] = self.inteligent_forbidden_time.to_alipay_dict()
            else:
                params['inteligent_forbidden_time'] = self.inteligent_forbidden_time
        if self.inteligent_use_times:
            if isinstance(self.inteligent_use_times, list):
                for i in range(0, len(self.inteligent_use_times)):
                    element = self.inteligent_use_times[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteligent_use_times[i] = element.to_alipay_dict()
            if hasattr(self.inteligent_use_times, 'to_alipay_dict'):
                params['inteligent_use_times'] = self.inteligent_use_times.to_alipay_dict()
            else:
                params['inteligent_use_times'] = self.inteligent_use_times
        if self.limit_rule:
            if hasattr(self.limit_rule, 'to_alipay_dict'):
                params['limit_rule'] = self.limit_rule.to_alipay_dict()
            else:
                params['limit_rule'] = self.limit_rule
        if self.min_consume:
            if hasattr(self.min_consume, 'to_alipay_dict'):
                params['min_consume'] = self.min_consume.to_alipay_dict()
            else:
                params['min_consume'] = self.min_consume
        if self.min_consume_condition:
            if hasattr(self.min_consume_condition, 'to_alipay_dict'):
                params['min_consume_condition'] = self.min_consume_condition.to_alipay_dict()
            else:
                params['min_consume_condition'] = self.min_consume_condition
        if self.pay_redirect_url:
            if hasattr(self.pay_redirect_url, 'to_alipay_dict'):
                params['pay_redirect_url'] = self.pay_redirect_url.to_alipay_dict()
            else:
                params['pay_redirect_url'] = self.pay_redirect_url
        if self.suit_shops:
            if isinstance(self.suit_shops, list):
                for i in range(0, len(self.suit_shops)):
                    element = self.suit_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suit_shops[i] = element.to_alipay_dict()
            if hasattr(self.suit_shops, 'to_alipay_dict'):
                params['suit_shops'] = self.suit_shops.to_alipay_dict()
            else:
                params['suit_shops'] = self.suit_shops
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentUseRule()
        if 'inteligent_forbidden_time' in d:
            o.inteligent_forbidden_time = d['inteligent_forbidden_time']
        if 'inteligent_use_times' in d:
            o.inteligent_use_times = d['inteligent_use_times']
        if 'limit_rule' in d:
            o.limit_rule = d['limit_rule']
        if 'min_consume' in d:
            o.min_consume = d['min_consume']
        if 'min_consume_condition' in d:
            o.min_consume_condition = d['min_consume_condition']
        if 'pay_redirect_url' in d:
            o.pay_redirect_url = d['pay_redirect_url']
        if 'suit_shops' in d:
            o.suit_shops = d['suit_shops']
        return o


