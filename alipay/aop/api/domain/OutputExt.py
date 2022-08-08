#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutputExt(object):

    def __init__(self):
        self._accessable = None
        self._desc = None
        self._field = None
        self._name = None

    @property
    def accessable(self):
        return self._accessable

    @accessable.setter
    def accessable(self, value):
        self._accessable = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, value):
        self._field = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.accessable:
            if hasattr(self.accessable, 'to_alipay_dict'):
                params['accessable'] = self.accessable.to_alipay_dict()
            else:
                params['accessable'] = self.accessable
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.field:
            if hasattr(self.field, 'to_alipay_dict'):
                params['field'] = self.field.to_alipay_dict()
            else:
                params['field'] = self.field
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
        o = OutputExt()
        if 'accessable' in d:
            o.accessable = d['accessable']
        if 'desc' in d:
            o.desc = d['desc']
        if 'field' in d:
            o.field = d['field']
        if 'name' in d:
            o.name = d['name']
        return o


