#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ForbbidenTime import ForbbidenTime
from alipay.aop.api.domain.UseTime import UseTime


class UseRule(object):

    def __init__(self):
        self._ext_info = None
        self._forbidden_time = None
        self._limit_rule = None
        self._min_consume = None
        self._pay_redirect_url = None
        self._suit_shops = None
        self._use_time = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def forbidden_time(self):
        return self._forbidden_time

    @forbidden_time.setter
    def forbidden_time(self, value):
        if isinstance(value, ForbbidenTime):
            self._forbidden_time = value
        else:
            self._forbidden_time = ForbbidenTime.from_alipay_dict(value)
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
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        if isinstance(value, list):
            self._use_time = list()
            for i in value:
                if isinstance(i, UseTime):
                    self._use_time.append(i)
                else:
                    self._use_time.append(UseTime.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.forbidden_time:
            if hasattr(self.forbidden_time, 'to_alipay_dict'):
                params['forbidden_time'] = self.forbidden_time.to_alipay_dict()
            else:
                params['forbidden_time'] = self.forbidden_time
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
        if self.use_time:
            if isinstance(self.use_time, list):
                for i in range(0, len(self.use_time)):
                    element = self.use_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_time[i] = element.to_alipay_dict()
            if hasattr(self.use_time, 'to_alipay_dict'):
                params['use_time'] = self.use_time.to_alipay_dict()
            else:
                params['use_time'] = self.use_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UseRule()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'forbidden_time' in d:
            o.forbidden_time = d['forbidden_time']
        if 'limit_rule' in d:
            o.limit_rule = d['limit_rule']
        if 'min_consume' in d:
            o.min_consume = d['min_consume']
        if 'pay_redirect_url' in d:
            o.pay_redirect_url = d['pay_redirect_url']
        if 'suit_shops' in d:
            o.suit_shops = d['suit_shops']
        if 'use_time' in d:
            o.use_time = d['use_time']
        return o


