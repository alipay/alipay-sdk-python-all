#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCampusBiztaskFinishModel(object):

    def __init__(self):
        self._channel_code = None
        self._task_bonus = None
        self._task_id = None
        self._task_type = None
        self._user_id = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def task_bonus(self):
        return self._task_bonus

    @task_bonus.setter
    def task_bonus(self, value):
        self._task_bonus = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.task_bonus:
            if hasattr(self.task_bonus, 'to_alipay_dict'):
                params['task_bonus'] = self.task_bonus.to_alipay_dict()
            else:
                params['task_bonus'] = self.task_bonus
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCampusBiztaskFinishModel()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'task_bonus' in d:
            o.task_bonus = d['task_bonus']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


