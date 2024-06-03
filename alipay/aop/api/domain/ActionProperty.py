#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActionProperty(object):

    def __init__(self):
        self._key = None
        self._material_instance_id = None
        self._type = None
        self._value = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def material_instance_id(self):
        return self._material_instance_id

    @material_instance_id.setter
    def material_instance_id(self, value):
        self._material_instance_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.material_instance_id:
            if hasattr(self.material_instance_id, 'to_alipay_dict'):
                params['material_instance_id'] = self.material_instance_id.to_alipay_dict()
            else:
                params['material_instance_id'] = self.material_instance_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActionProperty()
        if 'key' in d:
            o.key = d['key']
        if 'material_instance_id' in d:
            o.material_instance_id = d['material_instance_id']
        if 'type' in d:
            o.type = d['type']
        if 'value' in d:
            o.value = d['value']
        return o


