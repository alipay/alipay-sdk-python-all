#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessId(object):

    def __init__(self):
        self._source_id = None
        self._system_type = None

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def system_type(self):
        return self._system_type

    @system_type.setter
    def system_type(self, value):
        self._system_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.system_type:
            if hasattr(self.system_type, 'to_alipay_dict'):
                params['system_type'] = self.system_type.to_alipay_dict()
            else:
                params['system_type'] = self.system_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessId()
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'system_type' in d:
            o.system_type = d['system_type']
        return o


