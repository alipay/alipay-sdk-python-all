#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyAa import RainyAa


class RainyAAA(object):

    def __init__(self):
        self._object_havnt_name = None

    @property
    def object_havnt_name(self):
        return self._object_havnt_name

    @object_havnt_name.setter
    def object_havnt_name(self, value):
        if isinstance(value, RainyAa):
            self._object_havnt_name = value
        else:
            self._object_havnt_name = RainyAa.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.object_havnt_name:
            if hasattr(self.object_havnt_name, 'to_alipay_dict'):
                params['object_havnt_name'] = self.object_havnt_name.to_alipay_dict()
            else:
                params['object_havnt_name'] = self.object_havnt_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyAAA()
        if 'object_havnt_name' in d:
            o.object_havnt_name = d['object_havnt_name']
        return o


