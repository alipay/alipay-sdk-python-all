#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsMktObjectDTO(object):

    def __init__(self):
        self._obj_id = None
        self._type = None

    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.obj_id:
            if hasattr(self.obj_id, 'to_alipay_dict'):
                params['obj_id'] = self.obj_id.to_alipay_dict()
            else:
                params['obj_id'] = self.obj_id
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
        o = InsMktObjectDTO()
        if 'obj_id' in d:
            o.obj_id = d['obj_id']
        if 'type' in d:
            o.type = d['type']
        return o


