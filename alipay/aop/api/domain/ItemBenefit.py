#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemBenefit(object):

    def __init__(self):
        self._id = None
        self._key = None
        self._sub_key = None
        self._value = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def sub_key(self):
        return self._sub_key

    @sub_key.setter
    def sub_key(self, value):
        self._sub_key = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.sub_key:
            if hasattr(self.sub_key, 'to_alipay_dict'):
                params['sub_key'] = self.sub_key.to_alipay_dict()
            else:
                params['sub_key'] = self.sub_key
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
        o = ItemBenefit()
        if 'id' in d:
            o.id = d['id']
        if 'key' in d:
            o.key = d['key']
        if 'sub_key' in d:
            o.sub_key = d['sub_key']
        if 'value' in d:
            o.value = d['value']
        return o


