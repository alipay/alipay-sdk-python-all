#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SignInPrizeConfig import SignInPrizeConfig


class SignInBonusStrategy(object):

    def __init__(self):
        self._max_time = None
        self._min_time = None
        self._prizes = None
        self._signin_acc_type = None
        self._strategy_type = None

    @property
    def max_time(self):
        return self._max_time

    @max_time.setter
    def max_time(self, value):
        self._max_time = value
    @property
    def min_time(self):
        return self._min_time

    @min_time.setter
    def min_time(self, value):
        self._min_time = value
    @property
    def prizes(self):
        return self._prizes

    @prizes.setter
    def prizes(self, value):
        if isinstance(value, list):
            self._prizes = list()
            for i in value:
                if isinstance(i, SignInPrizeConfig):
                    self._prizes.append(i)
                else:
                    self._prizes.append(SignInPrizeConfig.from_alipay_dict(i))
    @property
    def signin_acc_type(self):
        return self._signin_acc_type

    @signin_acc_type.setter
    def signin_acc_type(self, value):
        self._signin_acc_type = value
    @property
    def strategy_type(self):
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, value):
        self._strategy_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_time:
            if hasattr(self.max_time, 'to_alipay_dict'):
                params['max_time'] = self.max_time.to_alipay_dict()
            else:
                params['max_time'] = self.max_time
        if self.min_time:
            if hasattr(self.min_time, 'to_alipay_dict'):
                params['min_time'] = self.min_time.to_alipay_dict()
            else:
                params['min_time'] = self.min_time
        if self.prizes:
            if isinstance(self.prizes, list):
                for i in range(0, len(self.prizes)):
                    element = self.prizes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prizes[i] = element.to_alipay_dict()
            if hasattr(self.prizes, 'to_alipay_dict'):
                params['prizes'] = self.prizes.to_alipay_dict()
            else:
                params['prizes'] = self.prizes
        if self.signin_acc_type:
            if hasattr(self.signin_acc_type, 'to_alipay_dict'):
                params['signin_acc_type'] = self.signin_acc_type.to_alipay_dict()
            else:
                params['signin_acc_type'] = self.signin_acc_type
        if self.strategy_type:
            if hasattr(self.strategy_type, 'to_alipay_dict'):
                params['strategy_type'] = self.strategy_type.to_alipay_dict()
            else:
                params['strategy_type'] = self.strategy_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignInBonusStrategy()
        if 'max_time' in d:
            o.max_time = d['max_time']
        if 'min_time' in d:
            o.min_time = d['min_time']
        if 'prizes' in d:
            o.prizes = d['prizes']
        if 'signin_acc_type' in d:
            o.signin_acc_type = d['signin_acc_type']
        if 'strategy_type' in d:
            o.strategy_type = d['strategy_type']
        return o


