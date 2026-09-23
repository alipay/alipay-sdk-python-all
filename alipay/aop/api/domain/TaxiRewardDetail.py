#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxiRewardDetail(object):

    def __init__(self):
        self._reward_amount = None
        self._reward_time = None

    @property
    def reward_amount(self):
        return self._reward_amount

    @reward_amount.setter
    def reward_amount(self, value):
        self._reward_amount = value
    @property
    def reward_time(self):
        return self._reward_time

    @reward_time.setter
    def reward_time(self, value):
        self._reward_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.reward_amount:
            if hasattr(self.reward_amount, 'to_alipay_dict'):
                params['reward_amount'] = self.reward_amount.to_alipay_dict()
            else:
                params['reward_amount'] = self.reward_amount
        if self.reward_time:
            if hasattr(self.reward_time, 'to_alipay_dict'):
                params['reward_time'] = self.reward_time.to_alipay_dict()
            else:
                params['reward_time'] = self.reward_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxiRewardDetail()
        if 'reward_amount' in d:
            o.reward_amount = d['reward_amount']
        if 'reward_time' in d:
            o.reward_time = d['reward_time']
        return o


