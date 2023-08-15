#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Schedule import Schedule


class AlipayCloudCloudbaseFunctionTriggerSetModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._function_name = None
        self._schedules = None
        self._trigger_name = None
        self._type = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def function_name(self):
        return self._function_name

    @function_name.setter
    def function_name(self, value):
        self._function_name = value
    @property
    def schedules(self):
        return self._schedules

    @schedules.setter
    def schedules(self, value):
        if isinstance(value, list):
            self._schedules = list()
            for i in value:
                if isinstance(i, Schedule):
                    self._schedules.append(i)
                else:
                    self._schedules.append(Schedule.from_alipay_dict(i))
    @property
    def trigger_name(self):
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, value):
        self._trigger_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.function_name:
            if hasattr(self.function_name, 'to_alipay_dict'):
                params['function_name'] = self.function_name.to_alipay_dict()
            else:
                params['function_name'] = self.function_name
        if self.schedules:
            if isinstance(self.schedules, list):
                for i in range(0, len(self.schedules)):
                    element = self.schedules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.schedules[i] = element.to_alipay_dict()
            if hasattr(self.schedules, 'to_alipay_dict'):
                params['schedules'] = self.schedules.to_alipay_dict()
            else:
                params['schedules'] = self.schedules
        if self.trigger_name:
            if hasattr(self.trigger_name, 'to_alipay_dict'):
                params['trigger_name'] = self.trigger_name.to_alipay_dict()
            else:
                params['trigger_name'] = self.trigger_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionTriggerSetModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'schedules' in d:
            o.schedules = d['schedules']
        if 'trigger_name' in d:
            o.trigger_name = d['trigger_name']
        if 'type' in d:
            o.type = d['type']
        return o


