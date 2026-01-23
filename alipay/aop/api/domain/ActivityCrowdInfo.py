#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityCrowdInfo(object):

    def __init__(self):
        self._crowd_rule_name = None
        self._crowd_type = None
        self._enterprise_id_list = None
        self._limit_type = None

    @property
    def crowd_rule_name(self):
        return self._crowd_rule_name

    @crowd_rule_name.setter
    def crowd_rule_name(self, value):
        self._crowd_rule_name = value
    @property
    def crowd_type(self):
        return self._crowd_type

    @crowd_type.setter
    def crowd_type(self, value):
        self._crowd_type = value
    @property
    def enterprise_id_list(self):
        return self._enterprise_id_list

    @enterprise_id_list.setter
    def enterprise_id_list(self, value):
        if isinstance(value, list):
            self._enterprise_id_list = list()
            for i in value:
                self._enterprise_id_list.append(i)
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_rule_name:
            if hasattr(self.crowd_rule_name, 'to_alipay_dict'):
                params['crowd_rule_name'] = self.crowd_rule_name.to_alipay_dict()
            else:
                params['crowd_rule_name'] = self.crowd_rule_name
        if self.crowd_type:
            if hasattr(self.crowd_type, 'to_alipay_dict'):
                params['crowd_type'] = self.crowd_type.to_alipay_dict()
            else:
                params['crowd_type'] = self.crowd_type
        if self.enterprise_id_list:
            if isinstance(self.enterprise_id_list, list):
                for i in range(0, len(self.enterprise_id_list)):
                    element = self.enterprise_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enterprise_id_list[i] = element.to_alipay_dict()
            if hasattr(self.enterprise_id_list, 'to_alipay_dict'):
                params['enterprise_id_list'] = self.enterprise_id_list.to_alipay_dict()
            else:
                params['enterprise_id_list'] = self.enterprise_id_list
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityCrowdInfo()
        if 'crowd_rule_name' in d:
            o.crowd_rule_name = d['crowd_rule_name']
        if 'crowd_type' in d:
            o.crowd_type = d['crowd_type']
        if 'enterprise_id_list' in d:
            o.enterprise_id_list = d['enterprise_id_list']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        return o


