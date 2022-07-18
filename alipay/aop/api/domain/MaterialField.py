#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaterialField(object):

    def __init__(self):
        self._field_name = None
        self._field_value = None

    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def field_value(self):
        return self._field_value

    @field_value.setter
    def field_value(self, value):
        if isinstance(value, list):
            self._field_value = list()
            for i in value:
                self._field_value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.field_value:
            if isinstance(self.field_value, list):
                for i in range(0, len(self.field_value)):
                    element = self.field_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.field_value[i] = element.to_alipay_dict()
            if hasattr(self.field_value, 'to_alipay_dict'):
                params['field_value'] = self.field_value.to_alipay_dict()
            else:
                params['field_value'] = self.field_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaterialField()
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'field_value' in d:
            o.field_value = d['field_value']
        return o


