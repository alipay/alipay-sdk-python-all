#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarUnionmemberTaskCallbackModel(object):

    def __init__(self):
        self._action_type = None
        self._manufacturer_id = None
        self._occur_time = None
        self._open_id = None
        self._task_type = None
        self._user_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def manufacturer_id(self):
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, value):
        self._manufacturer_id = value
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.manufacturer_id:
            if hasattr(self.manufacturer_id, 'to_alipay_dict'):
                params['manufacturer_id'] = self.manufacturer_id.to_alipay_dict()
            else:
                params['manufacturer_id'] = self.manufacturer_id
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayEcoMycarUnionmemberTaskCallbackModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'manufacturer_id' in d:
            o.manufacturer_id = d['manufacturer_id']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


