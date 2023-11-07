#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RedisInstanceInfo(object):

    def __init__(self):
        self._instance_id = None
        self._instance_name = None

    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def instance_name(self):
        return self._instance_name

    @instance_name.setter
    def instance_name(self, value):
        self._instance_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.instance_name:
            if hasattr(self.instance_name, 'to_alipay_dict'):
                params['instance_name'] = self.instance_name.to_alipay_dict()
            else:
                params['instance_name'] = self.instance_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RedisInstanceInfo()
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'instance_name' in d:
            o.instance_name = d['instance_name']
        return o


