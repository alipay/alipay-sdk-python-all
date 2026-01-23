#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityReward import ActivityReward


class CardOpenRewardInfo(object):

    def __init__(self):
        self._ldp_code = None
        self._rewards = None

    @property
    def ldp_code(self):
        return self._ldp_code

    @ldp_code.setter
    def ldp_code(self, value):
        self._ldp_code = value
    @property
    def rewards(self):
        return self._rewards

    @rewards.setter
    def rewards(self, value):
        if isinstance(value, list):
            self._rewards = list()
            for i in value:
                if isinstance(i, ActivityReward):
                    self._rewards.append(i)
                else:
                    self._rewards.append(ActivityReward.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ldp_code:
            if hasattr(self.ldp_code, 'to_alipay_dict'):
                params['ldp_code'] = self.ldp_code.to_alipay_dict()
            else:
                params['ldp_code'] = self.ldp_code
        if self.rewards:
            if isinstance(self.rewards, list):
                for i in range(0, len(self.rewards)):
                    element = self.rewards[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rewards[i] = element.to_alipay_dict()
            if hasattr(self.rewards, 'to_alipay_dict'):
                params['rewards'] = self.rewards.to_alipay_dict()
            else:
                params['rewards'] = self.rewards
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardOpenRewardInfo()
        if 'ldp_code' in d:
            o.ldp_code = d['ldp_code']
        if 'rewards' in d:
            o.rewards = d['rewards']
        return o


