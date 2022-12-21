#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VcpUniqueInfo(object):

    def __init__(self):
        self._unique_id = None
        self._unique_type = None

    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def unique_type(self):
        return self._unique_type

    @unique_type.setter
    def unique_type(self, value):
        self._unique_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        if self.unique_type:
            if hasattr(self.unique_type, 'to_alipay_dict'):
                params['unique_type'] = self.unique_type.to_alipay_dict()
            else:
                params['unique_type'] = self.unique_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpUniqueInfo()
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        if 'unique_type' in d:
            o.unique_type = d['unique_type']
        return o


