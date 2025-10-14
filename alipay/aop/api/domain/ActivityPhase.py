#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityReward import ActivityReward


class ActivityPhase(object):

    def __init__(self):
        self._award_status = None
        self._index = None
        self._ldp_code = None
        self._rewards = None
        self._target_count = None

    @property
    def award_status(self):
        return self._award_status

    @award_status.setter
    def award_status(self, value):
        self._award_status = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
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
    @property
    def target_count(self):
        return self._target_count

    @target_count.setter
    def target_count(self, value):
        self._target_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.award_status:
            if hasattr(self.award_status, 'to_alipay_dict'):
                params['award_status'] = self.award_status.to_alipay_dict()
            else:
                params['award_status'] = self.award_status
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
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
        if self.target_count:
            if hasattr(self.target_count, 'to_alipay_dict'):
                params['target_count'] = self.target_count.to_alipay_dict()
            else:
                params['target_count'] = self.target_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityPhase()
        if 'award_status' in d:
            o.award_status = d['award_status']
        if 'index' in d:
            o.index = d['index']
        if 'ldp_code' in d:
            o.ldp_code = d['ldp_code']
        if 'rewards' in d:
            o.rewards = d['rewards']
        if 'target_count' in d:
            o.target_count = d['target_count']
        return o


