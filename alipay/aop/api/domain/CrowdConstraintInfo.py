#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdConstraintInfo(object):

    def __init__(self):
        self._crowd_condition = None
        self._crowd_name = None
        self._crowd_restriction = None

    @property
    def crowd_condition(self):
        return self._crowd_condition

    @crowd_condition.setter
    def crowd_condition(self, value):
        self._crowd_condition = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def crowd_restriction(self):
        return self._crowd_restriction

    @crowd_restriction.setter
    def crowd_restriction(self, value):
        self._crowd_restriction = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_condition:
            if hasattr(self.crowd_condition, 'to_alipay_dict'):
                params['crowd_condition'] = self.crowd_condition.to_alipay_dict()
            else:
                params['crowd_condition'] = self.crowd_condition
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.crowd_restriction:
            if hasattr(self.crowd_restriction, 'to_alipay_dict'):
                params['crowd_restriction'] = self.crowd_restriction.to_alipay_dict()
            else:
                params['crowd_restriction'] = self.crowd_restriction
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdConstraintInfo()
        if 'crowd_condition' in d:
            o.crowd_condition = d['crowd_condition']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'crowd_restriction' in d:
            o.crowd_restriction = d['crowd_restriction']
        return o


