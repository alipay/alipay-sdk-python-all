#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RewardDTO(object):

    def __init__(self):
        self._reward_display_info = None
        self._reward_id = None

    @property
    def reward_display_info(self):
        return self._reward_display_info

    @reward_display_info.setter
    def reward_display_info(self, value):
        self._reward_display_info = value
    @property
    def reward_id(self):
        return self._reward_id

    @reward_id.setter
    def reward_id(self, value):
        self._reward_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.reward_display_info:
            if hasattr(self.reward_display_info, 'to_alipay_dict'):
                params['reward_display_info'] = self.reward_display_info.to_alipay_dict()
            else:
                params['reward_display_info'] = self.reward_display_info
        if self.reward_id:
            if hasattr(self.reward_id, 'to_alipay_dict'):
                params['reward_id'] = self.reward_id.to_alipay_dict()
            else:
                params['reward_id'] = self.reward_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RewardDTO()
        if 'reward_display_info' in d:
            o.reward_display_info = d['reward_display_info']
        if 'reward_id' in d:
            o.reward_id = d['reward_id']
        return o


