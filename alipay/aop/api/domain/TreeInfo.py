#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TreeInfo(object):

    def __init__(self):
        self._id = None
        self._instance_code = None
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def instance_code(self):
        return self._instance_code

    @instance_code.setter
    def instance_code(self, value):
        self._instance_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.instance_code:
            if hasattr(self.instance_code, 'to_alipay_dict'):
                params['instance_code'] = self.instance_code.to_alipay_dict()
            else:
                params['instance_code'] = self.instance_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TreeInfo()
        if 'id' in d:
            o.id = d['id']
        if 'instance_code' in d:
            o.instance_code = d['instance_code']
        if 'name' in d:
            o.name = d['name']
        return o


