#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsEndorseItem(object):

    def __init__(self):
        self._new_value = None
        self._old_value = None
        self._type = None

    @property
    def new_value(self):
        return self._new_value

    @new_value.setter
    def new_value(self, value):
        self._new_value = value
    @property
    def old_value(self):
        return self._old_value

    @old_value.setter
    def old_value(self, value):
        self._old_value = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_value:
            if hasattr(self.new_value, 'to_alipay_dict'):
                params['new_value'] = self.new_value.to_alipay_dict()
            else:
                params['new_value'] = self.new_value
        if self.old_value:
            if hasattr(self.old_value, 'to_alipay_dict'):
                params['old_value'] = self.old_value.to_alipay_dict()
            else:
                params['old_value'] = self.old_value
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
        o = InsEndorseItem()
        if 'new_value' in d:
            o.new_value = d['new_value']
        if 'old_value' in d:
            o.old_value = d['old_value']
        if 'type' in d:
            o.type = d['type']
        return o


