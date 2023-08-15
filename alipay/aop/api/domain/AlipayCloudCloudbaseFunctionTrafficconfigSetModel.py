#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficRule import TrafficRule


class AlipayCloudCloudbaseFunctionTrafficconfigSetModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._function_name = None
        self._traffic_rules = None

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
    def traffic_rules(self):
        return self._traffic_rules

    @traffic_rules.setter
    def traffic_rules(self, value):
        if isinstance(value, list):
            self._traffic_rules = list()
            for i in value:
                if isinstance(i, TrafficRule):
                    self._traffic_rules.append(i)
                else:
                    self._traffic_rules.append(TrafficRule.from_alipay_dict(i))


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
        if self.traffic_rules:
            if isinstance(self.traffic_rules, list):
                for i in range(0, len(self.traffic_rules)):
                    element = self.traffic_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.traffic_rules[i] = element.to_alipay_dict()
            if hasattr(self.traffic_rules, 'to_alipay_dict'):
                params['traffic_rules'] = self.traffic_rules.to_alipay_dict()
            else:
                params['traffic_rules'] = self.traffic_rules
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseFunctionTrafficconfigSetModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'function_name' in d:
            o.function_name = d['function_name']
        if 'traffic_rules' in d:
            o.traffic_rules = d['traffic_rules']
        return o


