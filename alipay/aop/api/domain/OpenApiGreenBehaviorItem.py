#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiGreenBehaviorItem(object):

    def __init__(self):
        self._behavior_id = None
        self._behavior_name = None
        self._behavior_time = None
        self._behavior_type = None
        self._biz_order_id = None
        self._carbon_value = None
        self._platform_code = None
        self._suggest_score = None

    @property
    def behavior_id(self):
        return self._behavior_id

    @behavior_id.setter
    def behavior_id(self, value):
        self._behavior_id = value
    @property
    def behavior_name(self):
        return self._behavior_name

    @behavior_name.setter
    def behavior_name(self, value):
        self._behavior_name = value
    @property
    def behavior_time(self):
        return self._behavior_time

    @behavior_time.setter
    def behavior_time(self, value):
        self._behavior_time = value
    @property
    def behavior_type(self):
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, value):
        self._behavior_type = value
    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def carbon_value(self):
        return self._carbon_value

    @carbon_value.setter
    def carbon_value(self, value):
        self._carbon_value = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def suggest_score(self):
        return self._suggest_score

    @suggest_score.setter
    def suggest_score(self, value):
        self._suggest_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior_id:
            if hasattr(self.behavior_id, 'to_alipay_dict'):
                params['behavior_id'] = self.behavior_id.to_alipay_dict()
            else:
                params['behavior_id'] = self.behavior_id
        if self.behavior_name:
            if hasattr(self.behavior_name, 'to_alipay_dict'):
                params['behavior_name'] = self.behavior_name.to_alipay_dict()
            else:
                params['behavior_name'] = self.behavior_name
        if self.behavior_time:
            if hasattr(self.behavior_time, 'to_alipay_dict'):
                params['behavior_time'] = self.behavior_time.to_alipay_dict()
            else:
                params['behavior_time'] = self.behavior_time
        if self.behavior_type:
            if hasattr(self.behavior_type, 'to_alipay_dict'):
                params['behavior_type'] = self.behavior_type.to_alipay_dict()
            else:
                params['behavior_type'] = self.behavior_type
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.carbon_value:
            if hasattr(self.carbon_value, 'to_alipay_dict'):
                params['carbon_value'] = self.carbon_value.to_alipay_dict()
            else:
                params['carbon_value'] = self.carbon_value
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.suggest_score:
            if hasattr(self.suggest_score, 'to_alipay_dict'):
                params['suggest_score'] = self.suggest_score.to_alipay_dict()
            else:
                params['suggest_score'] = self.suggest_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiGreenBehaviorItem()
        if 'behavior_id' in d:
            o.behavior_id = d['behavior_id']
        if 'behavior_name' in d:
            o.behavior_name = d['behavior_name']
        if 'behavior_time' in d:
            o.behavior_time = d['behavior_time']
        if 'behavior_type' in d:
            o.behavior_type = d['behavior_type']
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'carbon_value' in d:
            o.carbon_value = d['carbon_value']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'suggest_score' in d:
            o.suggest_score = d['suggest_score']
        return o


