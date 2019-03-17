#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentObjectRelationForOpenapi(object):

    def __init__(self):
        self._object_id = None
        self._object_type = None

    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value
    @property
    def object_type(self):
        return self._object_type

    @object_type.setter
    def object_type(self, value):
        self._object_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.object_id:
            if hasattr(self.object_id, 'to_alipay_dict'):
                params['object_id'] = self.object_id.to_alipay_dict()
            else:
                params['object_id'] = self.object_id
        if self.object_type:
            if hasattr(self.object_type, 'to_alipay_dict'):
                params['object_type'] = self.object_type.to_alipay_dict()
            else:
                params['object_type'] = self.object_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentObjectRelationForOpenapi()
        if 'object_id' in d:
            o.object_id = d['object_id']
        if 'object_type' in d:
            o.object_type = d['object_type']
        return o


