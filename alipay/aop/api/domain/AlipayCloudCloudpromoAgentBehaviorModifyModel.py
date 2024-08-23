#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoAgentBehaviorModifyModel(object):

    def __init__(self):
        self._behavior = None
        self._custom_id = None
        self._instance_id = None

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        self._behavior = value
    @property
    def custom_id(self):
        return self._custom_id

    @custom_id.setter
    def custom_id(self, value):
        self._custom_id = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior:
            if hasattr(self.behavior, 'to_alipay_dict'):
                params['behavior'] = self.behavior.to_alipay_dict()
            else:
                params['behavior'] = self.behavior
        if self.custom_id:
            if hasattr(self.custom_id, 'to_alipay_dict'):
                params['custom_id'] = self.custom_id.to_alipay_dict()
            else:
                params['custom_id'] = self.custom_id
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAgentBehaviorModifyModel()
        if 'behavior' in d:
            o.behavior = d['behavior']
        if 'custom_id' in d:
            o.custom_id = d['custom_id']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        return o


