#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityRewardConfig import ActivityRewardConfig


class ActivityReward(object):

    def __init__(self):
        self._reward_config = None
        self._unavailable_status = None
        self._use_status = None

    @property
    def reward_config(self):
        return self._reward_config

    @reward_config.setter
    def reward_config(self, value):
        if isinstance(value, ActivityRewardConfig):
            self._reward_config = value
        else:
            self._reward_config = ActivityRewardConfig.from_alipay_dict(value)
    @property
    def unavailable_status(self):
        return self._unavailable_status

    @unavailable_status.setter
    def unavailable_status(self, value):
        self._unavailable_status = value
    @property
    def use_status(self):
        return self._use_status

    @use_status.setter
    def use_status(self, value):
        self._use_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.reward_config:
            if hasattr(self.reward_config, 'to_alipay_dict'):
                params['reward_config'] = self.reward_config.to_alipay_dict()
            else:
                params['reward_config'] = self.reward_config
        if self.unavailable_status:
            if hasattr(self.unavailable_status, 'to_alipay_dict'):
                params['unavailable_status'] = self.unavailable_status.to_alipay_dict()
            else:
                params['unavailable_status'] = self.unavailable_status
        if self.use_status:
            if hasattr(self.use_status, 'to_alipay_dict'):
                params['use_status'] = self.use_status.to_alipay_dict()
            else:
                params['use_status'] = self.use_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityReward()
        if 'reward_config' in d:
            o.reward_config = d['reward_config']
        if 'unavailable_status' in d:
            o.unavailable_status = d['unavailable_status']
        if 'use_status' in d:
            o.use_status = d['use_status']
        return o


